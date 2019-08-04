from youtube_dl import YoutubeDL
import vlc
from time import sleep
import wx
import wx.adv
import random
from threading import Thread

random.seed(version=2)



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
        #create_menu_item(menu, 'bassboost', self.bassBeats)
        create_menu_item(menu, 'trap music', self.trapBeats)
        create_menu_item(menu, 'underground', self.underBeats)
        create_menu_item(menu, 'rap/trap', self.rapBeats)
        create_menu_item(menu, 'hip-hop', self.hipBeats)
        #create_menu_item(menu, 'ncs', self.ncsBeats)
        create_menu_item(menu, 'cxdy beats', self.cxdyBeats)
        create_menu_item(menu, 'feniko beats', self.fenikoBeats)
        create_menu_item(menu, 'feniko 2019', self.feniko2019Beats)
        create_menu_item(menu, 'feniko 2018', self.feniko2018Beats)
        create_menu_item(menu, 'feniko free', self.fenikofreeBeats)
        menu.AppendSeparator()
        create_menu_item(menu, 'Exit', self.on_exit)
        return menu

    def cxdyBeats(self,event):
        if(Vars.Mode!='cxdy'):
            try:
                Vars.player.stop()
                Vars.playlistPlayer.kill()
            except:
                pass
            YouPlay('https://www.youtube.com/playlist?list=PLNj1VGi-TF3AIJAJKr4WZDQDOyj6nY4sK',isPlaylist=True)
            Vars.Mode='cxdy'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'cxdy beats')
            Vars.ModeName='cxdy beats'

    def fenikoBeats(self,event):
        if(Vars.Mode!='feniko'):
            try:
                Vars.player.stop()
                Vars.playlistPlayer.kill()
            except:
                pass
            YouPlay('https://www.youtube.com/playlist?list=PLpfvdY_eWAh3cSkndJKrfor_ip929wqfn',isPlaylist=True)
            Vars.Mode='feniko'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'feniko beats')
            Vars.ModeName='feniko beats'


    def feniko2019Beats(self,event):
        if(Vars.Mode!='feniko2019'):
            try:
                Vars.player.stop()
                Vars.playlistPlayer.kill()
            except:
                pass
            YouPlay('https://www.youtube.com/playlist?list=PLpfvdY_eWAh2xnLcfBIi20lc4G1Ypr-1M',isPlaylist=True)
            Vars.Mode='feniko2019'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'feniko 2019')
            Vars.ModeName='feniko 2019'

    def feniko2018Beats(self,event):
        if(Vars.Mode!='feniko2018'):
            try:
                Vars.player.stop()
                Vars.playlistPlayer.kill()
            except:
                pass
            YouPlay('https://www.youtube.com/playlist?list=PLpfvdY_eWAh2qs67AsMda-qT9aaaSZraT',isPlaylist=True)
            Vars.Mode='feniko2018'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'feniko 2018')
            Vars.ModeName='feniko 2018'

    def fenikofreeBeats(self,event):
        if(Vars.Mode!='fenikofree'):
            try:
                Vars.player.stop()
                Vars.playlistPlayer.kill()
            except:
                pass
            YouPlay('https://www.youtube.com/playlist?list=PLpfvdY_eWAh2NxE0PGesVXVSTQNZzvKbu',isPlaylist=True)
            Vars.Mode='fenikofree'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'feniko free')
            Vars.ModeName='feniko free'

    def hipBeats(self,event):
        if(Vars.Mode!='hip'):
            try:
                Vars.player.stop()
                Vars.playlistPlayer.kill()
            except:
                pass
            YouPlay('https://www.youtube.com/watch?v=DU97WQY_GLs')
            Vars.Mode='hip'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'hip-hop')
            Vars.ModeName='hip-hop'

    def rapBeats(self,event):
        if(Vars.Mode!='rap'):
            try:
                Vars.player.stop()
                Vars.playlistPlayer.kill()
            except:
                pass
            YouPlay('https://www.youtube.com/watch?v=-WOA1Dr2EUo')
            Vars.Mode='rap'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'rap/trap')
            Vars.ModeName='rap/trap'

    def underBeats(self,event):
        if(Vars.Mode!='under'):
            try:
                Vars.player.stop()
                Vars.playlistPlayer.kill()
            except:
                pass
            YouPlay('https://www.youtube.com/watch?v=05689ErDUdM')
            Vars.Mode='under'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'underground')
            Vars.ModeName='underground'

    def trapBeats(self,event):
        if(Vars.Mode!='trap'):
            try:
                Vars.player.stop()
                Vars.playlistPlayer.kill()
            except:
                pass
            YouPlay('https://www.youtube.com/watch?v=Ppnogeufi-4')
            Vars.Mode='trap'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'trap music')
            Vars.ModeName='trap music'

    def bassBeats(self,event):
        if(Vars.Mode!='bass'):
            try:
                Vars.player.stop()
                Vars.playlistPlayer.kill()
            except:
                pass
            YouPlay('https://www.youtube.com/watch?v=CtwD3joN1as')
            Vars.Mode='bass'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'bassboost')
            Vars.ModeName='bassboost'


    def studyBeats(self,event):
        if(Vars.Mode!='study'):
            try:
                Vars.player.stop()
                Vars.playlistPlayer.kill()
            except:
                pass
            YouPlay('https://www.youtube.com/watch?v=hHW1oY26kxQ')
            Vars.Mode='study'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'relax/study')
            Vars.ModeName='relax/study'


    def chillBeats(self,event):
        if(Vars.Mode!='chill'):
            try:
                Vars.player.stop()
                Vars.playlistPlayer.kill()
            except:
                pass
            YouPlay('https://www.youtube.com/watch?v=EcEMX-63PKY')
            Vars.Mode='chill'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'chill/sleep')
            Vars.ModeName='chill/sleep'


    def sadBeats(self,event):
        if(Vars.Mode!='sad'):
            try:
                Vars.player.stop()
                Vars.playlistPlayer.kill()
            except:
                pass
            YouPlay('https://www.youtube.com/watch?v=yPLLhlX0YXM')
            Vars.Mode='sad'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'sad/sleepy')
            Vars.ModeName='sad/sleepy'


    def gamingBeats(self,event):
        if(Vars.Mode!='gaming'):
            try:
                Vars.player.stop()
                Vars.playlistPlayer.kill()
            except:
                pass
            YouPlay('https://www.youtube.com/watch?v=8ptZkxgcj7I')
            Vars.Mode='gaming'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'gaming')
            Vars.ModeName='gaming'


    def electronicBeats(self,event):
        if(Vars.Mode!='electronic'):
            try:
                Vars.player.stop()
                Vars.playlistPlayer.kill()
            except:
                pass
            YouPlay('https://www.youtube.com/watch?v=oZzQC8NVTeM')
            Vars.Mode='electronic'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'electronic')
            Vars.ModeName='electronic'


    def dubstepBeats(self,event):
        if(Vars.Mode!='dubstep'):
            try:
                Vars.player.stop()
                Vars.playlistPlayer.kill()
            except:
                pass
            YouPlay('https://www.youtube.com/watch?v=GVC5adzPpiE')
            Vars.Mode='dubstep'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'dubstep/trap/edm')
            Vars.ModeName='dubstep/trap/edm'


    def ncsBeats(self,event):
        if(Vars.Mode!='ncs'):
            try:
                Vars.player.stop()
                Vars.playlistPlayer.kill()
            except:
                pass
            YouPlay('https://www.youtube.com/watch?v=Jb16xUBDY-4')
            Vars.Mode='ncs'
            icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon, 'ncs')
            Vars.ModeName='ncs'



    def on_left_down(self, event):
        try:
            Vars.player.audio_toggle_mute()
            isMuted = Vars.player.audio_get_mute()
            if(isMuted):
                icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
                self.SetIcon(icon, Vars.ModeName+"(muted)")
            else:
                icon = wx.Icon('PYStream.ico', wx.BITMAP_TYPE_ICO)
                self.SetIcon(icon, Vars.ModeName)
        except:
            pass



    def on_exit(self, event):
        wx.CallAfter(self.Destroy)
        self.frame.Close()

class App(wx.App):
    def OnInit(self):
        frame=wx.Frame(None)
        self.SetTopWindow(frame)
        TaskBarIcon(frame)
        return True



def YouPlay(vidUrl,isPlaylist=False):

    VIDEO_URL = vidUrl
    ydl_opt={"extract_flat":True,'quiet':True}
    ydl = YoutubeDL(ydl_opt)
    ydl.add_default_info_extractors()

    if(not isPlaylist):
        info = ydl.extract_info(VIDEO_URL,download=False)
        title=info['title']
        print(title)
        url = info['formats'][0]['url']

        instance = vlc.Instance('--no-video --quiet')
        Vars.player = instance.media_player_new()
        media = instance.media_new(url)
        Vars.player.set_media(media)

        Vars.player.play()
    else:
        ydl_opt={"extract_flat":True,'quiet':True,'playlistrandom':True}
        ydl = YoutubeDL(ydl_opt)
        info = ydl.extract_info(VIDEO_URL,download=False)
        entries=info['entries']
        Vars.playlistPlayer=PlaylistPlaying(Vars.player, entries)
        Vars.playlistPlayer.start()


class PlaylistPlaying(Thread):
    def __init__(self,player,playlist):
        Thread.__init__(self)
        self.playlist=playlist

    def run(self):
        while True:
            i=random.randint(0,len(self.playlist))
            print("https://youtube.com/watch?v="+self.playlist[i]['url'])
            YouPlay("https://youtube.com/watch?v="+self.playlist[i]['url'])
            self.player=Vars.player
            while self.player.get_state()!=6:
                sleep(0.7)


class Vars:
    Mode=''
    player=None
    isStopped=False
    ModeName=''
    playlistPlayer=None

def main():
    app = App(False)
    app.MainLoop()

main()
