import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk

class MyApplication(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.anewchallenger.ANewChallenger")
        GLib.set_application_name("A New Challenger")

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self, title="A New Challenger", default_size=(1024, 768))
        window.present()


app = MyApplication()

exit_status = app.run(sys.argv)
sys.exit(exit_status)