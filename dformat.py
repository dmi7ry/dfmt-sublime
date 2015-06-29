import sublime, sublime_plugin, os, shutil, tempfile

plugin_settings = None

def read_settings(key, default):
    global plugin_settings
    if plugin_settings is None:
        plugin_settings = sublime.load_settings("dformat.sublime-settings")

    return sublime.active_window().active_view().settings().get(key, plugin_settings.get(key, default))

class dformat(sublime_plugin.TextCommand):

    def run(self, edit):
        # get temporary directory
        tmpdir = tempfile.mkdtemp("", "_dfmt_temp_")
        name = tmpdir + "\\sublime_dfmt_tmp.d"

        # check config file
        config_path = read_settings("config_path", "")
        if os.path.isfile(config_path):
            # print "Config path: " + config_path
            try:
                shutil.copy(config_path, tmpdir)
            except IOError:
                sublime.status_message("Can't copy config file to " + path)
                pass

        # print "[DFormat] Save text to file: " + name

        # get text from current view
        all_text = sublime.Region(0, self.view.size())
        text = self.view.substr(all_text)

        # save text
        f = open(name, "w")
        f.write(text)
        f.close()

        # run dfmt
        res = os.system(r"dfmt --inplace " + f.name)
        if res == 0:
            # clear view
            self.view.erase(edit, all_text)

            #read new text
            f = open(name)
            formated = f.read()
            f.close()

            self.view.insert(edit, 0, formated)

            msg = "[DFormat] Formating finished"
        else:
            msg = "[DFormat] dfmt error (dfmt.exe not found?)"

        # remove temporary file and dir
        shutil.rmtree(tmpdir)

        sublime.status_message(msg)
