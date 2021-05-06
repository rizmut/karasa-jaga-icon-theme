#!/bin/python3

import os
import sys

mapping = {
    'org.xfce.about': 'help-about',
    'org.xfce.appfinder': 'edit-find',
    'org.xfce.catfish': 'catfish',
    'org.xfce.Dictionary': 'xfce4-dict',
    'org.xfce.filemanager': 'system-file-manager',
    'org.xfce.genmon': 'utilities-system-monitor',
    'org.xfce.gigolo': 'gtk-network',
    'org.xfce.mailreader': 'emblem-mail',
    'org.xfce.mousepad': 'accessories-text-editor',
    'org.xfce.notification': 'xfce4-notifyd',
    'org.xfce.panel.actions': 'system-log-out',
    'org.xfce.panel.applicationsmenu': 'xfce4-panel-menu',
    'org.xfce.panel.clock': 'x-office-calendar',
    'org.xfce.panel.directorymenu': 'folder',
    'org.xfce.panel.launcher': 'application-x-executable',
    'org.xfce.panel.pager': 'xfce4-workspaces',
    'org.xfce.panel.separator': 'list-remove-symbolic',
    'org.xfce.panel.showdesktop': 'user-desktop',
    'org.xfce.panel.tasklist': 'preferences-system-windows',
    'org.xfce.panel.windowmenu': 'preferences-system-windows',
    'org.xfce.panel': 'xfce4-panel',
    'org.xfce.parole': 'parole',
    'org.xfce.powermanager': 'xfce4-power-manager-settings',
    'org.xfce.ristretto': 'ristretto',
    'org.xfce.ScreenSaver': 'preferences-desktop-screensaver',
    'org.xfce.screenshooter': 'applets-screenshooter',
    'org.xfce.session': 'xfce4-session',
    'org.xfce.settings.accessibility': 'preferences-desktop-accessibility',
    'org.xfce.settings.appearance': 'preferences-desktop-theme',
    'org.xfce.settings.color': 'xfce4-color-settings',
    'org.xfce.settings.default-applications': 'preferences-desktop-default-applications',
    'org.xfce.settings.display': 'video-display',
    'org.xfce.settings.editor': 'preferences-system',
    'org.xfce.settings.keyboard': 'preferences-desktop-keyboard',
    'org.xfce.settings.manager': 'preferences-desktop',
    'org.xfce.settings.mouse': 'preferences-desktop-peripherals',
    'org.xfce.taskmanager': 'utilities-system-monitor',
    'org.xfce.terminal-settings': 'utilities-terminal',
    'org.xfce.terminal': 'utilities-terminal',
    'org.xfce.terminalemulator': 'utilities-terminal',
    'org.xfce.thunar': 'Thunar',
    'org.xfce.volman': 'drive-removable-media',
    'org.xfce.webbrowser': 'web-browser',
    'org.xfce.workspaces': 'xfce4-workspaces',
    'org.xfce.xfburn': 'xfburn',
    'org.xfce.xfdashboard': 'xfdashboard',
    'org.xfce.xfdesktop': 'preferences-desktop-wallpaper',
    'org.xfce.xfmpc': 'multimedia-player',
    'org.xfce.xfwm4-tweaks': 'wmtweaks',
    'org.xfce.xfwm4': 'xfwm4',
    'xfsm-hibernate': 'system-suspend-hibernate',
    'xfsm-lock': 'system-lock-screen',
    'xfsm-logout': 'system-log-out',
    'xfsm-reboot': 'system-reboot',
    'xfsm-shutdown': 'system-shutdown',
    'xfsm-suspend': 'system-suspend',
    'xfsm-switch-user': 'system-users'
}

valueMapping = {}
for k, v in mapping.items():
    if v not in list(valueMapping.keys()):
        valueMapping[v] = []
    valueMapping[v].append(k)

def getAppsPath(root, path):
    subpath = path.replace(root, "", 1)
    parts = subpath.split("/")[:-1]
    parts = parts[-2:]
    try:
        if parts[0] != "scalable":
            int(parts[0].replace("x", "").replace("@", ""))
        cat = parts[1]
    except:
        cat = parts[0]
    apps = "apps"
    if "org.xfce" not in path:
        if "action" in cat or "xfsm-switch-user" in path:
            apps = "actions"
    if "@" in cat:
        basecat = cat.split("@")[0]
        apps = cat.replace(basecat, apps)
    appsdir = path.replace("/%s/" % cat, "/%s/" % apps)
    return appsdir

if __name__ == "__main__":
    folder = sys.argv[-1]
    if not os.path.isdir(folder):
        print("Path is not a folder")
        sys.exit(1)
    
    for root, dirs, files in os.walk(folder, topdown=False):
        for name in files:
            basename, ext = os.path.splitext(name)
            if basename in list(valueMapping.keys()):
                path = os.path.join(root, name)
                for link in valueMapping[basename]:
                    linkname = "%s%s" % (link, ext)
                    linkpath = os.path.join(root, linkname)
                    linkappspath = getAppsPath(folder, linkpath)
                    appsdir = os.path.dirname(linkappspath)
                    linkrelpath = os.path.relpath(path, appsdir)
                    if not os.path.exists(appsdir):
                        os.makedirs(os.path.dirname(linkappspath))
                    if not os.path.exists(linkappspath):
                        os.symlink(linkrelpath, linkname)
                        os.rename(linkname, linkappspath)
