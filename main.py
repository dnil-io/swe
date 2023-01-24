from mp import MpThread

thread = MpThread(1, "Thread-1", 1)

thread.start()

BaseContext = testingcontext.getInteractive()
