try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

def flash(event):
    v = d.get(event.char.upper())
    if v is not None:
        d[event.char.upper()] = (v[0]+1, v[1])
        v[1].config(bg='green')
        root.after(500, lambda: v[1].config(bg = 'lightgrey'))
    
root = tk.Tk()
root['bg'] = 'green'
lf = tk.LabelFrame(root, text=" Keyboard ", bd=3)
lf.pack(padx=15, pady=15)
# typical keyboard layout
l_list = [
'^',  '1',  '2',  '3',  '4', '5' , '6', '7', '8', '9', '0', 'ß', '`', 'BACKSPACE',
'TAB', 'Q',  'W',  'E',  'R', 'T', 'Z', 'U', 'I', 'O', 'P', 'Ü', '+', 'RETURN',
'CAPSLOCK',  'A',  'S',  'D',  'F', 'G', 'H', 'J', 'K', 'L', 'Ö', 'Ä', '\'',
'LSHIFT',  '<',  'Y',  'X',  'C', 'V', 'B', 'N', 'M', ',', '.', '-', 'RSHIFT',
'LCONTROL', 'WINDOWS', 'ALT', 'SPACE', 'ALT G', 'WINDOWS', 'FN', 'RCONTROL']
# create and position all buttons with a for-loop
# r, c used for row, column grid values
r = 1
c = 0
n = 0
# list(range()) needed for Python3
d = {}
f = list(range(len(l_list)))
for label in l_list:
    # create the label
    w = 80
    h = 80
    if label=='BACKSPACE':
	    w = 160
    if label=='TAB':
        w = 120
    if label=='RETURN':
        w = 120
        h = 160
    if label=='CAPSLOCK':
        w = 140
    if label=='LSHIFT':
        w = 100
        c = 0
        r += 80
    if label=='RSHIFT':
        w = 220
    if label=='LCONTROL' or label=='RCONTROL' or label=='ALT' or label=='ALT G' or label=='WINDOWS' or label=='FN':
        w = 100
    if label=='SPACE':
        w = 500
        
    f[n] = tk.Frame(lf, width=w, height=h)
    f[n].grid_propagate(False) #disables resizing of frame
    f[n].columnconfigure(0, weight=1) #enables button to fill frame
    f[n].rowconfigure(0,weight=1)

    l = tk.Label(f[n], text=label, width=w, height=h, borderwidth=1, relief='raised')
    
    d[label] = (0, l)
    
    # position the button
    f[n].grid(row=r, column=c, rowspan=h, columnspan=w)
    l.grid(sticky="wens")
    # increment button index
    n += 1
    # update row/column position
    c += w
    if c > 14 * 80:
        c = 0
        r += 80
        
root.bind('<Key>', flash)
root.mainloop()