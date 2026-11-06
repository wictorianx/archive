#SingleInstance Force
#MaxThreadsPerHotkey 3

clickDelay := 5


ESC::
	Toggle := !Toggle
	While (Toggle) {
		MouseClick, Left
		Sleep clickDelay
	}
	Return