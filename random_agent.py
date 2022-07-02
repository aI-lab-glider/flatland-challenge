import numpy as np
from flatland.envs.rail_env import RailEnv
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

env = RailEnv(width=30, height=30)
obs = env.reset()
axs = plt.subplot()


def make_step():
    while True:
        obs, rew, done, info = env.step({
            0: np.random.randint(0, 5),
            1: np.random.randint(0, 5)
        })
        yield env.render()
        if all(done.values()):
            break


def animate(frame):
    im.set_data(frame)


im = axs.imshow(env.render())
ani = FuncAnimation(plt.gcf(), animate, frames=make_step,
                    interval=1, repeat=False)
plt.show()
