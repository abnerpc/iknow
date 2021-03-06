#!/usr/bin/env python
import wx


class Iknow(wx.Frame):
    """a simple app to fool around"""

    def __init__(self, parent):
        style = wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER
        wx.Frame.__init__(self, parent, size=(600, 160), style=style)

        self.dummy_text = "This is only one sentence for test"
        self.changing = False
        self.answer = ''

        self.InitUI()

    def InitUI(self):
        """ build screen components """

        self.panel = wx.Panel(self)

        self.lbl_quote = wx.StaticText(self.panel, label="Question", pos=(20, 30))

        self.txt_quote = wx.TextCtrl(self.panel, pos=(20, 50), size=(560, 20))
        self.Bind(wx.EVT_TEXT, self.OnTextChange, self.txt_quote)

        self.btn_answer = wx.Button(self.panel, label="Answer", pos=(240, 100), size=(120, 50))
        self.Bind(wx.EVT_BUTTON, self.OnAnswerClick, self.btn_answer)
        self.btn_again = wx.Button(self.panel, label="Again", pos=(240, 100), size=(120, 50))
        self.btn_again.Hide()
        self.Bind(wx.EVT_BUTTON, self.OnAgainClick, self.btn_again)

        self.lbl_labelAnswer = wx.StaticText(self.panel, label="Answer:", pos=(20, 140))
        self.lbl_answer = wx.StaticText(self.panel, pos=(75, 140))

        self.SetTitle("Iknow")
        self.Centre()
        self.Show(True)

    def OnTextChange(self, e):

        l_pos = self.txt_quote.GetLastPosition()
        str_question = e.GetString()
        chr_n = str_question[l_pos - 1: l_pos]

        if not self.changing:
            if len(str_question) == 1 and ord(chr_n) == 92:
                self.txt_quote.Clear()
                self.changing = True
        else:
            if ord(chr_n) == 92:
                self.txt_quote.Replace(l_pos - 1, l_pos, '')
                self.changing = False
                return
            self.txt_quote.Replace(l_pos - 1, l_pos, self.dummy_text[l_pos - 1])
            self.answer += chr_n

        #print l_pos
        #print ord(chr_n)
        #print self.answer

    def OnAnswerClick(self, e):
        if self.txt_quote.IsEmpty():
            return
        self.btn_answer.Hide()
        self.btn_again.Show()
        self.SetSizeWH(600, 200)
        self.lbl_answer.SetLabel(self.answer)

    def OnAgainClick(self, e):
        self.btn_again.Hide()
        self.btn_answer.Show()
        self.SetSizeWH(600, 160)
        self.lbl_answer.SetLabel('')


def main():

    ex = wx.App(False)
    Iknow(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()
