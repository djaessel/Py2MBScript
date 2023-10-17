# This Python file uses the following encoding: utf-8


class AnimationSequence:
    def __init__(self, duration : float, resource_name : str, beginning_frame : int, ending_frame : int):
        self.duration = duration
        self.resource_name = resource_name
        self.beginning_frame = beginning_frame
        self.ending_frame = ending_frame


    # TODO: flags
    # TODO: extra values


class Animation:
    def __init__(self, id : str):
        self.id = id
        self.flags = []
        self.masterFlags = []
        self.sequences = []


    def add_sequence(self, sequence : AnimationSequence):
        self.sequences.append(sequence)

