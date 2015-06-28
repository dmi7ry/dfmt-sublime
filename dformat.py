import sublime, sublime_plugin, os

class dformat(sublime_plugin.TextCommand):
    def run(self, edit):

        # get windows temporary directory
        p = "WINDIR"
        if p in os.environ:
            path = os.path.join(os.environ[p], "temp")
        else:
            path = ''

        name = path + '\\sublime_dfmt_tmp'

        # print "[DFormat] Save text to file: " + name

        # get text from current view
        all_text = sublime.Region(0, self.view.size())
        text = self.view.substr(all_text)

        # save text
        f = open(name, 'w')
        f.write(text)
        f.close()

        # run dfmt
        os.system(r'dfmt --inplace ' + f.name)

        # clear view
        self.view.erase(edit, all_text)

        #read new text
        f = open(name)
        formated = f.read()
        f.close()

        self.view.insert(edit, 0, formated)

        # remove temporary file
        os.remove(name)
