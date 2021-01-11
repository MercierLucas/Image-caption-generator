from IPython.display import clear_output


class ProgressBar:
    def __init__(self,n_steps,size):
        self.size = size
        self.steps = n_steps
        self.last_step = 0

    def update(self,epoch):
        clamp = int(epoch/self.size * self.steps)

        if clamp != self.last_step:
            self.last_step = clamp
            perc = epoch/self.size * 100

            txt = "="*clamp+ " "*(self.steps-clamp)
            print(f"[{txt}]{perc:.0f}%")
            clear_output(wait=True)