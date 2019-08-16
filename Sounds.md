# Nomenklatura

melodyka – wyznacza następstwo dźwięków o różnej wysokości i różnym czasie trwania,  
rytmika – porządkuje materiał dźwiękowy w czasie,  
dynamika – reguluje natężenie dźwięku,  
tempo (agogika) – określa szybkość utworu,  BPM 
artykulacja – określa sposób wydobywania dźwięku,  
harmonika – porządkuje współbrzmienia dźwięków w utworze,  
kolorystyka – określa barwę dźwięku.  

matrum:
tempo 96 BPM - jeśli zwiekszasz tempo to automatycznie jej czas będzie się skracał    
dal 96 BPM Ćwierćnuta = 625 ms,  Ósemka trwa 313 ms

ile wartosc i takcie / jakie wartosci w takcie  
3/4   625 * 3 = takt trwa 1875 ms    
6/8    czyli  313 * 6 = 1878 ms.    
4/4   652ms * 4  = takt trwa  2500 ms    

 
frazy 4/8/16 taktowe 


# UE4

new engine is called audioMixer  

`source` is defined to be the thing in the audio engine which actually generates audio in the audio renderer.  
`Source Effects` - audio effect which applies to a single source. (a filter, a delay, an envelope, distortion,  ... )  
 `source effect chain`   use it among any number of sources.  

` submix` is simply a mix of individual sources (post spatialization) into a single buffer.  

` submix effect`  


`Source Buses` and` Source Bus Effects`  

https://learningsynths.ableton.com/oscillators/how-synths-make-sound  
