# Nomenklatura

melodyka – wyznacza następstwo dźwięków o różnej wysokości i różnym czasie trwania,  
rytmika – porządkuje materiał dźwiękowy w czasie,  
dynamika – reguluje natężenie dźwięku,  
agogika (tempo) – określa szybkość utworu,  
artykulacja – określa sposób wydobywania dźwięku,  
harmonika – porządkuje współbrzmienia dźwięków w utworze,  
kolorystyka – określa barwę dźwięku.  

matrum:
tempo 96
 jeśli zmienisz tempo, w góre to automatycznie jej czas będzie się skracał
3/4  Ćwirćnuta trwa  625 ms Czyli cały takt trwa 625 * 3  -= 1875 ms
4/4   652ms * 4  =  2500 ms
6/8   Ósemka trwa 313 ms czyli  313 * 6 = 1878 ms.

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
