def make_readable(seconds):
    hours = seconds // 3600
    minutes = seconds // 60 - hours * 60
    seconds = seconds - minutes * 60 - hours * 3600
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)
seconds = 309844
make_readable(seconds)
print(make_readable(seconds))

#   return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)