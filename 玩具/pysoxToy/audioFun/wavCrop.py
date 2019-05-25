import sox

# create transformer
tfm = sox.Transformer()
# trim the audio between 5 and 10.5 seconds.
tfm.trim(0,14.2)
# apply compression
tfm.compand()
# apply a fade in and fade out
tfm.fade(fade_in_len=1.0, fade_out_len=0.5)
# create the output file.
tfm.build('./orig/1111.wav', './orig/1111Clip.wav')
# see the applied effects
tfm.effects_log