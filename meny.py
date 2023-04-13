import PySimpleGUI as g

lists_in_list = [
    [g.Text("введите имя"), g.InputText(key="name")],
    [g.Text("выбери размер"), g.OptionMenu(values=[16, 32, 64, 128, 256, "1000-7"], default_value=64, key="size")],
    [g.Button("старт", key="start"), g.Button("поддержи меня", key="pleas"), g.Button("выход", key="bye")],
    [g.Radio("WASD", key="wasd", group_id=1), g.Radio("-> <- ", key="strel", group_id=1)],
    [g.Text("выбери размер экрана"), g.OptionMenu(values=[1/2, 1/4, 1/1], default_value=1.0, key="skreen_size")]
]
windows_11 = g.Window("вэлком ту сантропэ", lists_in_list)

while True:
    reed = windows_11.read()
    s_reed = reed[0]
    z_reed = reed[1]
    print(s_reed, z_reed)

    if s_reed == "bye" or s_reed == "start":
        break
