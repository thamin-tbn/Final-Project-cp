
import math
# محاسبه تعداد دور اولیه و ثانویه ترانس و سطح مقطع هسته بر حسب cm2
def calT(V1,V2,I1,Flux_density=1):
    
    Prim_Volt_Amps=V1*I1 
    Core_Area = 1.15 * math.sqrt(Prim_Volt_Amps)
    Turns_per_volt = 1 / (4.44 * .0001 * Core_Area *50 *  Flux_density) 
    Prim_Turns = Turns_per_volt * V1
    Sec_Turns = Turns_per_volt * V2 * 1.03
    return Prim_Turns,Sec_Turns,Core_Area



V1=220
V2=380
I1=1

print(calT(V1,V2,I1))

