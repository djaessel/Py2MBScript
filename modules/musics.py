# This Python file uses the following encoding: utf-8

from music import MusicTrack, TrackFlag


track1 = MusicTrack("mount_and_blade_title_screen", "mount_and_blade_title_screen.ogg")
track1.add_flag(TrackFlag.SIT_MAIN_TITLE)
track1.add_flag(TrackFlag.START_IMMEDIATELY)

# TODO: add more from original game
