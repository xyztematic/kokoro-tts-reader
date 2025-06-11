from kokoro import KPipeline
import soundfile as sf
import torch, os, glob, time, sched
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader



class MyApp(App):
    
    s = sched.scheduler(time.time, time.sleep)
    
    def on_text(self, instance, value):
        self.TTStext = value
        
    def deleteOldAudio(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        fileList = glob.glob(os.path.join(dir_path, "*.wav"))
        for filePath in fileList:
            try:
                os.remove(filePath)
            except:
                print("Error while deleting file : ", filePath)
                
    def readAudioSnippedAsync(self, instance):
        if (self.currentAudioSnippet >= len(self.generated_audio)): return
        sound = self.loadedSoundFiles[self.currentAudioSnippet]
        self.currentAudioSnippet += 1
        if sound:
            sound.play()
            self.s.enter(sound.length - .2, 1, self.readAudioSnippedAsync, argument=("",))
            if (not self.s.empty()): self.s.run()
        else: return
    
    def produceAndReadAudio(self, instance):
        if self.TTStext == "": return
        self.deleteOldAudio()
        pipeline = KPipeline(lang_code='a')
        generator = pipeline(self.TTStext, voice='af_heart')
        self.generated_audio = []
        for i, (gs, ps, audio) in enumerate(generator):
            sf.write(f'{i}.wav', audio, 24000)
            self.generated_audio.append(f'{i}.wav')
            
        self.currentAudioSnippet = 0
        self.loadedSoundFiles = []
        for audio in self.generated_audio:
            self.loadedSoundFiles.append(SoundLoader.load(audio))
        
        self.readAudioSnippedAsync("")
                
                
            
    def build(self):
        layout = GridLayout(cols=1)
        textinput = TextInput(size_hint=(1.0, .95), pos=(0, 0))
        textinput.bind(text=self.on_text)
        button = Button(text='Read', size_hint=(1.0, .05), pos=(0, 0))
        button.bind(on_press=self.produceAndReadAudio)
        layout.add_widget(textinput)
        layout.add_widget(button)
        self.TTStext = ""
        
        return layout


            
if __name__ == '__main__':
    MyApp().run()