# Problem Statement: Hackocalypse

## **Scenario Overview**
Welcome to the apocalypse — where zombies roam the streets, supplies are scarce, and survivors look to *your AI system* for hope. Your task? To prove that brains (yours) can outsmart brains-eating zombies (theirs).

The city is in chaos, thanks to a mysterious outbreak that has turned ordinary life into a survival horror movie. Survivors are scattered, resources are limited, and the undead are... well, let's just say they're not here to make friends. In this dire situation, your AI will be humanity's lifeline.

Your system must excel at two critical tasks:
1. **Base Map Knowledge**  
   - Process a detailed text description of the city layout.  
   - This includes streets, highways, buildings, potential shelters, resource locations, and evacuation routes. Think of it as building a mental map of the apocalypse.

2. **Real-Time Dynamic Updates**  
   - Integrate live updates on zombie movements, weather hazards, resource availability, and shifting safe zones.  
   - This stream of updates will keep your AI on its toes — because zombies certainly won’t wait for your system to catch up.

The survival of the human race depends on your AI’s ability to process and combine this static and dynamic data into a coherent, actionable strategy. No pressure.

---

### **Scenario Types**
Your system will be tested against the following scenario types:

1. **Urban Evacuation**
   - Plan escape routes through a maze of city streets while avoiding collapsed buildings, blocked roads, and (of course) zombies.  
   - Zombies like to hang around high-value targets, so be prepared for surprises.

2. **Resource Management**
   - Supplies are scarce, so every decision counts. Should survivors go for that food stash across the street or save their energy?  
   - Manage limited resources wisely while weighing risk vs reward.

3. **Weather Hazards**
   - Navigate through storms, floods, and reduced visibility. Zombies may not mind the weather, but survivors sure do.  
   - Prepare for environmental challenges that will make survival even trickier.

4. **Zombie Patterns**
   - Zombies aren’t exactly rocket scientists, but they do have predictable movement patterns. Use this to your advantage — most of the time.  
   - Occasionally, zombies might get a little spicy and exhibit unexpected behavior. Keep your system ready for anything.

---

### **Your Task**
Your challenge is to build a **Retrieval-Augmented Generation (RAG)** system using the Groq API that expertly handles this complex information landscape. The system should:  
- Maintain constant awareness of the city layout.  
- Process and remember real-time updates as they stream in.  
- Generate **clear, actionable survival plans** that take into account all available information.  

In short: your AI must juggle static maps, dynamic chaos, and the occasional zombie curveball—all while keeping survivors alive.

---

Remember: Your AI might be the only thing standing between survivors and zombie dinner. Make it count.