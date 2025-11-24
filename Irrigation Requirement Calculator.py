import tkinter as tk
import math

def calculate():
    try:
        t=float(e_t.get())
        rh=float(e_rh.get())
        u=float(e_u.get())
        rs=float(e_rs.get())
        kc=float(e_kc.get())
        area=float(e_area.get())
        rain=float(e_rain.get())
        eff=float(e_eff.get())
        days=float(e_days.get())
        max_depth=float(e_max.get())
    except Exception as ex:
        v_eto.set("err")
        v_etc.set("err")
        v_net.set("err")
        v_gross.set("err")
        v_vol.set("err")
        v_events.set("0")
        v_pemm.set("0")
        v_pevol.set("0")
        return
    eto_val=0.408*rs-0.7*(rh/100.0)+0.1*u+0.05*t
    etc_mm=eto_val*kc*days
    net_ir_mm=etc_mm-rain
    if net_ir_mm<0:
        net_ir_mm=0.0
    gross_ir_mm=net_ir_mm/(eff/100.0) if eff>0 else 0.0
    volume_m3=gross_ir_mm/1000.0*area
    events=math.ceil(gross_ir_mm/max_depth) if max_depth>0 and gross_ir_mm>0 else 0
    per_event_mm=gross_ir_mm/events if events>0 else 0.0
    per_event_volume_m3=per_event_mm/1000.0*area
    v_eto.set(f"{eto_val:.3f}")
    v_etc.set(f"{etc_mm:.3f}")
    v_net.set(f"{net_ir_mm:.3f}")
    v_gross.set(f"{gross_ir_mm:.3f}")
    v_vol.set(f"{volume_m3:.3f}")
    v_events.set(str(events))
    v_pemm.set(f"{per_event_mm:.3f}")
    v_pevol.set(f"{per_event_volume_m3:.3f}")

root=tk.Tk()
root.title("Irrigation Calculator")
labels=["Temperature (C)","Relative Humidity (%)","Wind speed (m/s)","Solar radiation (MJ/m2/day)","Crop coefficient (Kc)","Area (m2)","Rainfall (mm)","Efficiency (%)","Days","Max depth per event (mm)"]
defaults=["30","60","2","18","1.1","10000","5","70","7","50"]
entries=[]
for i,lbl in enumerate(labels):
    tk.Label(root,text=lbl).grid(row=i,column=0,sticky="w",padx=4,pady=2)
    ent=tk.Entry(root)
    ent.grid(row=i,column=1,padx=4,pady=2)
    ent.insert(0,defaults[i])
    entries.append(ent)
e_t,e_rh,e_u,e_rs,e_kc,e_area,e_rain,e_eff,e_days,e_max=entries
btn=tk.Button(root,text="Calculate",command=calculate)
btn.grid(row=len(labels),column=0,columnspan=2,pady=6)
out_labels=["ETO (mm/day)","ETc (mm)","Net irrigation (mm)","Gross irrigation (mm)","Total volume (m3)","Events","Per event (mm)","Per event volume (m3)"]
vars_list=[]
for i,ol in enumerate(out_labels):
    tk.Label(root,text=ol).grid(row=i,column=2,sticky="w",padx=8,pady=2)
    var=tk.StringVar()
    tk.Label(root,textvariable=var,width=14,relief="sunken").grid(row=i,column=3,padx=4,pady=2)
    vars_list.append(var)
v_eto,v_etc,v_net,v_gross,v_vol,v_events,v_pemm,v_pevol=vars_list
root.mainloop()
