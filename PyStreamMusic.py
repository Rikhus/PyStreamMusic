import youtube_dl
import vlc
from time import sleep
import wx
import wx.adv



def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.AppendItem(item)
    return item

class TaskBarIcon(wx.adv.TaskBarIcon):
    def __init__(self, frame):
        self.frame = frame
        super(TaskBarIcon, self).__init__()

        icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon, 'PyStreamMusic')

        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.on_left_down)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        create_menu_item(menu, 'relax/study', self.studyBeats)
        create_menu_item(menu, 'chill/sleep', self.chillBeats)
        create_menu_item(menu, 'sad/sleepy', self.sadBeats)
        create_menu_item(menu, 'gaming', self.gamingBeats)
        create_menu_item(menu, 'electronic', self.electronicBeats)
        create_menu_item(menu, 'dubstep/trap/edm', self.dubstepBeats)
        create_menu_item(menu, 'bassboost', self.bassBeats)
        create_menu_item(menu, 'trap music', self.trapBeats)
        create_menu_item(menu, 'underground', self.underBeats)
        create_menu_item(menu, 'rap/trap', self.rapBeats)
        create_menu_item(menu, 'hip-hop', self.hipBeats)
        create_menu_item(menu, 'ncs', self.ncsBeats)
        menu.AppendSeparator()
        create_menu_item(menu, 'Exit', self.on_exit)
        return menu

    def hipBeats(self,event):
        if(Vars.Mode!='hip'):
            try:
                Vars.player.stop()
            except:
                pass
            YouPlay('https://www.youtube.com/watch?v=DU97WQY_GLs')
            Vars.Mode='hip'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'hip-hop')

    def rapBeats(self,event):
        if(Vars.Mode!='rap'):
            try:
                Vars.player.stop()
            except:
                pass
            YouPlay('https://www.youtube.com/watch?v=-WOA1Dr2EUo')
            Vars.Mode='rap'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'rap/trap')

    def underBeats(self,event):
        if(Vars.Mode!='under'):
            try:
                Vars.player.stop()
            except:
                pass
            YouPlay('https://www.youtube.com/watch?v=05689ErDUdM')
            Vars.Mode='under'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'underground')

    def trapBeats(self,event):
        if(Vars.Mode!='trap'):
            try:
                Vars.player.stop()
            except:
                pass
            YouPlay('https://www.youtube.com/watch?v=Ppnogeufi-4')
            Vars.Mode='trap'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'trap music')

    def bassBeats(self,event):
        if(Vars.Mode!='bass'):
            try:
                Vars.player.stop()
            except:
                pass
            YouPlay('https://www.youtube.com/watch?v=CtwD3joN1as')
            Vars.Mode='bass'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'bassboost')

    def studyBeats(self,event):
        if(Vars.Mode!='study'):
            try:
                Vars.player.stop()
            except:
                pass
            YouPlay('https://www.youtube.com/watch?v=hHW1oY26kxQ')
            Vars.Mode='study'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'relax/study')

    def chillBeats(self,event):
        if(Vars.Mode!='chill'):
            try:
                Vars.player.stop()
            except:
                pass
            YouPlay('https://www.youtube.com/watch?v=EcEMX-63PKY')
            Vars.Mode='chill'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'chill/sleep')

    def sadBeats(self,event):
        if(Vars.Mode!='sad'):
            try:
                Vars.player.stop()
            except:
                pass
            YouPlay('https://www.youtube.com/watch?v=yPLLhlX0YXM')
            Vars.Mode='sad'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'sad/sleepy')

    def gamingBeats(self,event):
        if(Vars.Mode!='gaming'):
            try:
                Vars.player.stop()
            except:
                pass
            YouPlay('https://www.youtube.com/watch?v=8ptZkxgcj7I')
            Vars.Mode='gaming'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'gaming')

    def electronicBeats(self,event):
        if(Vars.Mode!='electronic'):
            try:
                Vars.player.stop()
            except:
                pass
            YouPlay('https://www.youtube.com/watch?v=oZzQC8NVTeM')
            Vars.Mode='electronic'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'electronic')

    def dubstepBeats(self,event):
        if(Vars.Mode!='dubstep'):
            try:
                Vars.player.stop()
            except:
                pass
            YouPlay('https://www.youtube.com/watch?v=GVC5adzPpiE')
            Vars.Mode='dubstep'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'dubstep/trap/edm')

    def ncsBeats(self,event):
        if(Vars.Mode!='ncs'):
            try:
                Vars.player.stop()
            except:
                pass
            YouPlay('https://www.youtube.com/watch?v=Jb16xUBDY-4')
            Vars.Mode='ncs'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'ncs')


    def on_left_down(self, event):
        Vars.player.audio_toggle_mute()


    def on_exit(self, event):
        wx.CallAfter(self.Destroy)
        self.frame.Close()

class App(wx.App):
    def OnInit(self):
        frame=wx.Frame(None)
        self.SetTopWindow(frame)
        TaskBarIcon(frame)
        return True



def YouPlay(vidUrl):
    VIDEO_URL = vidUrl

    ydl = youtube_dl.YoutubeDL()
    video = ydl.extract_info(
        VIDEO_URL,
        download=False,
    )
    title=video['title']
    print(title)
    url = video['url']

    instance = vlc.Instance('--no-video')
    Vars.player = instance.media_player_new()
    media = instance.media_new(url)
    Vars.player.set_media(media)

    Vars.player.play()


class Vars:
    Mode='study'
    player=None
    isStopped=False

def main():
    app = App(False)
    app.MainLoop()

main()
