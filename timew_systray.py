import dearpygui.dearpygui as dpg
import time
import asyncio
import subprocess

rows=['status','start','Current','Total']
def save_callback():
    print("Save Clicked")

def dpg_init():
    dpg.create_context()
    dpg.create_viewport(width=400,height=100,decorated=False,disable_close=True,min_width=0,min_height=0,x_pos=-1)
    dpg.set_viewport_always_top(True)
    dpg.setup_dearpygui()


    with dpg.window(label='',no_scrollbar=True,min_size=[0,0],autosize=True,no_title_bar=True,no_background=True,no_collapse=True):
        for r in rows:
            dpg.add_text(default_value=r,tag=r)

    dpg.show_viewport()
    dpg.render_dearpygui_frame()
async def dpg_loop():
    while dpg.is_dearpygui_running():
        dpg.render_dearpygui_frame()
        await asyncio.sleep(1)
    dpg.destroy_context()

async def checktimew():
    while True:
        tw=subprocess.run(['timew'],capture_output=True)
        if tw.returncode == 0:
            rw=tw.stdout.split(b'\n')
            for i,e in enumerate(rows):
                dpg.configure_item(e,default_value=rw[i],show=True)
        else:
            dpg.configure_item('status',default_value="Tracker off")
            for i in range(3):
                dpg.configure_item(rows[i+1],show=False)
        await asyncio.sleep(15)
        # print('Hello sleepy...')

async def main():
    print('Hello ...')
    dpg_init()
    await asyncio.sleep(1)
    print('... World!')
    await asyncio.gather(
       dpg_loop(),
       #checksleep(),
       checktimew()
       )



asyncio.run(main())
