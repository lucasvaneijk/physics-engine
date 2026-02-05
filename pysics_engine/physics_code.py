import customtkinter as ctk
import math 

elements = ["h", "he", "li", "be", "b", "c", "n", "o", "f", "ne", "na", "mg", "al", "si", "p", "s", "cl", "ar", "k", "ca", "sc", "ti", "v", "cr", "mn", "fe", "co", "ni", "cu", "zn", "ga", "ge", "as", "se", "br", "kr", "rb", "sr", "y", "zr", "nb", "mo", "tc", "ru", "rh", "pd", "ag", "cd", "in", "sn", "sb", "te", "i", "xe", "cs", "ba", "la", "ce", "pr", "nd", "pm", "sm", "eu", "gd", "tb", "dy", "ho", "er", "tm", "yb", "lu", "hf", "ta", "w", "re", "os", "ir", "pt", "au", "hg", "tl", "pb", "bi", "po", "at", "rn", "fr", "ra", "ac", "th", "pa", "u", "np", "pu", "am", "cm", "bk", "cf", "es", "fm", "md", "no", "lr", "rf", "db", "sg", "bh", "hs", "mt", "ds", "rg", "cn", "nh", "fl", "mc", "lv", "ts", "og"]

gravity = 0 # this is the gravity

power_down = 0 #these are the powers 
power_up = 0
power_left = 0
power_right = 0
power_forward = 0
power_backward = 0

height = 0 #the height at were it will be dropped
weight = 0 #the weight of the object

ctk.set_appearance_mode("system") 
ctk.set_default_color_theme("blue")


class Welcomepage(ctk.CTkFrame):
    def __init__(self, controller, parent):
        super().__init__(parent)
        

        welcome_label = ctk.CTkLabel(self, text="welcome to my homepage choose one of my projects")
        welcome_label.pack(pady=50)

        physics_button = ctk.CTkButton(self, text="physics engine",
                                        command=lambda: controller.show_frame("calculator"))
        physics_button.pack(pady=50)
        
        science_button = ctk.CTkButton(self, text="sience project", 
                                       command=lambda: controller.show_frame("science_entry(still expirimental)")
        science_button.pack(pady=25)
        
        


class calculator(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        # -- grid configure --
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=2)
        self.grid_columnconfigure(3, weight=3)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=2)
        self.grid_rowconfigure(3, weight=3)

        # ---- State ----
        self.gravity = 0

        self.power_down = 0.0
        self.power_up = 0.0
        self.power_left = 0.0
        self.power_right = 0.0
        self.power_forward = 0.0
        self.power_backward = 0.0

        self.height = 0.0
        self.weight = 0.0

        # ---- power down ----
        self.power_down_label = ctk.CTkLabel(self, text="power down.")
        self.power_down_label.grid(row=0, column=2, padx=10, pady=3, sticky="we")
        
        self.power_down_entry = ctk.CTkEntry(self, placeholder_text="how many newtons down?", height=20, width=300)
        self.power_down_entry.bind("<Return>", self.power_down_entry._entry_focus_out())
        self.power_down_entry.grid(row=1, column=2, padx=10, pady=3, sticky="we")
        # ----- power up -----
        self.power_up_label = ctk.CTkLabel(self, text="power up")
        self.power_up_label.grid(row=2, column=2, padx=10, pady=3, sticky="we")

        self.power_up_entry = ctk.CTkEntry(self, placeholder_text="how many newtons up?", width=300, height=20)
        self.power_up_entry.bind("<Return>", self.power_up_entry._entry_focus_out())
        self.power_up_entry.grid(row=3, column=2, padx=10, pady=3, sticky="we")
        # ---- power left ----
        self.power_left_label = ctk.CTkLabel(self, text="power left")
        self.power_left_label.grid(row=4, column=2, padx=4, pady=3, sticky="we")

        self.power_left_entry = ctk.CTkEntry(self, placeholder_text="how many newtons left?", width=300, height=20)
        self.power_left_entry.bind("<Return>", self.power_left_entry._entry_focus_out())
        self.power_left_entry.grid(row=5, column=2, padx=10, pady=3, sticky="we")
        # ---- power right ----
        power_right_label = ctk.CTkLabel(self, text="power right")
        power_right_label.grid(row=6, column=2, padx=10, pady=3, sticky="we")

        self.power_right_entry = ctk.CTkEntry(self, placeholder_text="how many newtons right?", width=300, height=20)
        self.power_right_entry.bind("<Return>", self.power_right_entry._entry_focus_out())
        self.power_right_entry.grid(row=7, column=2, padx=10, pady=3, sticky="we")
        # --- power forwards ---
        self.power_forward_label = ctk.CTkLabel(self, text="power forwards:")
        self.power_forward_label.grid(row=8, column=2, padx=10, pady=3, sticky="we")

        self.power_forward_entry = ctk.CTkEntry(self, placeholder_text="how many newtons forwards?", height=20, width=300)
        self.power_forward_entry.bind("<Return>", self.power_forward_entry._entry_focus_out())
        self.power_forward_entry.grid(row=9, column=2, padx=10, pady=3, sticky="we")
        # --- power backwards ---
        self.power_backward_label = ctk.CTkLabel(self, text="power backwards")
        self.power_backward_label.grid(row=10, column=2, padx=10, pady=3, sticky="we")

        self.power_backward_entry = ctk.CTkEntry(self, placeholder_text="how many newtons backwards?", height=20, width=300)
        self.power_backward_entry.bind("<Return>", self.power_backward_entry._entry_focus_out())
        self.power_backward_entry.grid(row=11, column=2, padx=10, pady=3, sticky="we")
        # ------ height ------
        self.height_label = ctk.CTkLabel(self, text="height")
        self.height_label.grid(row=12, column=2, padx=10, pady=3, sticky="we")

        self.height_entry = ctk.CTkEntry(self, placeholder_text="how high will it be dropped? (base is 1)", height=20, width=300)
        self.height_entry.bind("<Return>", self.height_entry._entry_focus_out())
        self.height_entry.grid(row=13, column=2, padx=10, pady=3, sticky="we")
        # ------ weight ------
        self.weight_label = ctk.CTkLabel(self, text="weight")
        self.weight_label.grid(row=14, column=2, padx=10, pady=3, sticky="we")

        self.weight_entry = ctk.CTkEntry(self, placeholder_text="how many kg does it weigh? (base is 1)", width=300, height=20)
        self.weight_entry.bind("<Return>", self.weight_entry._entry_focus_out())
        self.weight_entry.grid(row=15, column=2, padx=10, pady=3, sticky="we")
        # ----- gravity -----
        self.gravity_label = ctk.CTkLabel(self, text="gravity")
        self.gravity_label.grid(row=16, column=2, padx=10, pady=3, sticky="we")

        self.gravity_entry = ctk.CTkEntry(self, placeholder_text="how much gravity will there be (base is 9.81)", height=20, width=300)
        self.gravity_entry.bind("<Return>", self.gravity_entry._entry_focus_out())
        self.gravity_entry.grid(row=17, column=2, padx=10, pady=3, sticky="we")

        self.results_label = ctk.CTkLabel(self, text="enter your numbers")
        self.results_label.grid(row=18, column=2, padx=10, pady=3, sticky="we")

        self.calculate_button = ctk.CTkButton(self, text="calculate physics", command=self.calculate)
        self.calculate_button.grid(row=19, column=2, padx=10, pady=10, sticky="we")

        self.back_button = ctk.CTkButton(self, text="back", height=5, width=10, command=lambda: controller.show_frame("Welcomepage"))
        self.back_button.grid(row=0, column=0, padx=1, pady=10, sticky="e")

    # ---- Event handlers ----
    def enter_press(self, event):
        self.calculate()

    # ---- Read number ----
    def _read_number(self, entry, min_val, max_val, placeholder, name):
    
        raw = entry.get().strip()
        
        if raw == "":
            val = 0.0
        else:
            try:
                val = float(raw)
            except ValueError:
                # Not a number
                entry._entry_focus_out()
                return None, f"{name}: not a number"

        # reachcontrol
        if not (min_val <= val <= max_val):
            entry._entry_focus_out()
            return None, f"{name}: out of range [{min_val}, {max_val}]"
        
        entry._entry_focus_out()
        return val, None


    # ---- Core ----
    def calculate(self):
        errors = []
        self.gravity = 0

        self.power_down = 0.0
        self.power_up = 0.0
        self.power_left = 0.0
        self.power_right = 0.0
        self.power_forward = 0.0
        self.power_backward = 0.0

        self.height = 0.0
        self.weight = 0.0

        # powers (N)
        v, e = self._read_number(self.power_down_entry, -10000, 10000, "how many newtons down?", "down force")
        if e: errors.append(e)
        else: self.power_down += v

        v, e = self._read_number(self.power_up_entry, -10000, 10000, "how many newtons up?", "up force")
        if e: errors.append(e)
        else: self.power_down -= v

        v, e = self._read_number(self.power_left_entry, -10000, 10000, "how many newtons left?", "left force")
        if e: errors.append(e)
        else: self.power_left += v

        v, e = self._read_number(self.power_right_entry, -10000, 10000, "how many newtons right?", "right force")
        if e: errors.append(e)
        else: self.power_left -= (v * -1)  

        v, e = self._read_number(self.power_forward_entry, -10000, 10000, "how many newtons forwards?", "forward force")
        if e: errors.append(e)
        else: self.power_forward += v

        v, e = self._read_number(self.power_backward_entry, -10000, 10000, "how many newtons backwards?", "backwards force")
        if e: errors.append(e)
        else: self.power_forward -= (v * -1)  

        
        v, e = self._read_number(self.height_entry, 0, 10000, "how high will it be dropped?", "height (m)")
        if e: errors.append(e)
        else:
            if v < 1 :
                self.height += 1
            else: self.height += v


        v, e = self._read_number(self.weight_entry, 0.0, 10000, "how many kg does it weigh?", "mass (kg)")
        if e: errors.append(e)
        else:
            if v == 0:
                self.weight += 1
            else: self.weight += v
        
        v, e = self._read_number(self.gravity_entry, 0.0, 1000, "how much gravity will there be (base is 9.81)", "gravity (m/s²)")
        if e: errors.append(e)
        else:
            if v == 0:
                self.gravity = 9.81
            else:
                self.gravity += v
    
        if errors:
            self.results_label.configure(text="; ".join(errors))
            return
        



        result_page = self.controller.frames["resultpage"]
        result_page.update_results(
            power_down=self.power_down,
            power_left=self.power_left,
            power_forward=self.power_forward,
            height=self.height,
            mass=self.weight,
            gravity=self.gravity)
        
        # to resultpage
        self.controller.show_frame("resultpage")


        



class resultpage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # UI 
        self.title_label = ctk.CTkLabel(self, text="calculation results", font=("Arial", 20))
        self.title_label.pack(pady=15)

        self.inputs_label = ctk.CTkLabel(self, text="Inputs: (waiting)")
        self.inputs_label.pack(pady=8)

        self.acc_label = ctk.CTkLabel(self, text="Accelerations: (waiting)")
        self.acc_label.pack(pady=8)

        self.time_label = ctk.CTkLabel(self, text="Time to ground: (waiting)")
        self.time_label.pack(pady=8)

        self.pos_label = ctk.CTkLabel(self, text="Impact position (x, y): (waiting)")
        self.pos_label.pack(pady=8)

        self.back_button = ctk.CTkButton(self, text="Back to calculator",
                                        command=lambda: self.controller.show_frame("calculator"))

        self.back_button.pack(pady=15)

    def update_results(self, power_down, power_left, power_forward, height, mass, gravity):
        """
          Fv = power_down + mass*gravity
          a_v = Fv / mass
          a_x = power_left / mass
          a_y = power_forwards / mass
          t = sqrt(2*height / a_v) (alleen als a_v>0 en height>0)
          x = 0.5*a_x*t^2
          y = 0.5*a_y*t^2
        """
        # Inputs tonen
        self.inputs_label.configure(
            text=(
                "Inputs:\n"
                f"  mass = {mass} kg\n"
                f"  height = {height} m\n"
                f"  gravity = {gravity} m/s²\n"
                f"  net forces: down={power_down:} N, left={power_left} N, forwards={power_forward} N"
            )
        )

        # Massa check
        if mass <= 0:
            self.acc_label.configure(text="Accelerations: mass must be > 0")
            self.time_label.configure(text="Time to ground: undefined (invalid mass)")
            self.pos_label.configure(text="Impact position: undefined")
            return

        # Accelerations
        F_vertical = power_down + mass * gravity
        a_vertical = F_vertical / mass
        a_x = power_left / mass
        a_y = power_forward / mass

        self.acc_label.configure(
            text=(
                "Accelerations:\n"
                f"  a_vertical = {a_vertical} m/s²\n"
                f"  a_x (left +) = {a_x} m/s²\n"
                f"  a_y (forwards +) = {a_y} m/s²"
            )
        )

        # Time + position
        if  a_vertical >= 0 and height > 0:
            t = math.sqrt(2.0 * height / a_vertical)
            x = 0.5 * a_x * t * t
            y = 0.5 * a_y * t * t
            self.time_label.configure(text=f"Time to ground: t = {t} s")
            self.pos_label.configure(text=f"Impact position: x = {x} m, y = {y} m")
        else:
            self.time_label.configure(text="Time to ground: undefined (a_vertical ≤ 0 or height ≤ 0)")
            self.pos_label.configure(text="Impact position: undefined (no fall)")


class science_entry(ctk.CTkFrame):
    def __init__(self, controller, parent):
        super().__init__(parent)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=2)
        self.grid_columnconfigure(3, weight=3)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=2)
        self.grid_rowconfigure(3, weight=3)

        self.science_title = ctk.CTkLabel(self, text="enter your elements to fix")
        self.science_title.grid(row=0, column=1, padx=10, pady=10, sticky="we")

        
        self.science_name_entry_1 = ctk.CTkEntry(self, placeholder_text="enter the name of the first element here", width=300)
        self.science_name_entry_1.grid(row=1, column=0, padx=10, pady=8, sticky="e")
        
        self.science_name_entry_2 = ctk.CTkEntry(self, placeholder_text="enter the name of the second element here", width=100)
        self.science_name_entry_2.grid(row=1, column=1, padx=10, pady=8, sticky="we")

        self.science_name_entry_3 = ctk.CTkEntry(self, placeholder_text="enter the name of your third element here", width=100)
        self.science_name_entry_3.grid(row=1, column=2, padx=10, pady=8, sticky="we" )

        self.science_arrow_down = ctk.CTkLabel(self, text="↓", font=("arial", 60))
        self.science_arrow_down.grid(row=2, column=1, padx=10, pady=10, sticky="we")

        self.science_output_name_entry_1 = ctk.CTkEntry(self, placeholder_text="enter the first output element here", width=300)
        self.science_output_name_entry_1.grid(row=3, column=0, padx=10, pady=8, sticky="e")
        
        self.science_output_name_entry_2 = ctk.CTkEntry(self, placeholder_text="enter your second output element here", width=100)
        self.science_output_name_entry_2.grid(row=3, column=1, padx=10, pady=8, sticky="we")
        
        self.science_output_name_entry_3 = ctk.CTkEntry(self, placeholder_text="enter your third output element here", width=100)
        self.science_output_name_entry_3.grid(row=3, column=2, padx=10, pady=8, sticky="we")

        self.science_fix_button = ctk.CTkButton(self, text="fix", command=lambda: self.extract_elements())
        self.science_fix_button.grid(row=4, column=1, padx=10, pady=10, sticky="we")

    def read_elements(self, entry, name, sort):
        print("hallo")
        raw = entry.get().strip()

        if raw =="":
            val = None
        else:
            try:
                val = float(raw)
            except ValueError:
                if sort == "entry":
                    return None, f"the {name} entry is not an number" 
                else:
                    return None, f"the {name} output is not an number"
        if not val in elements:
            return None, f"the {name} is not an element"
        
        print(raw)
        return val, None
    
    def extract_elements(self):
        errors = []
        self.science_entry_1 = 0
        self.science_entry_2 = 0
        self.science_entry_3 = 0
        self.science_output_1 = 0
        self.science_output_2 = 0
        self.science_output_3 = 0
        print(self.science_arrow_down)

        v, e = self.read_elements(self.science_name_entry_1, "first", "entry")
        if e: errors.append(e)

        print(errors)


        if errors:
            self.science_title.configure("; ".join(errors))
            return
        
        
    




class science_resultpage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        
        





class main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("physics engine")
        self.geometry("2400x1200")

        # Container for pages
        container = ctk.CTkFrame(self, corner_radius=0)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Frames register
        self.frames = {}
        for F in (Welcomepage, calculator, resultpage, science_entry, science_resultpage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Startpage
        self.show_frame("Welcomepage")

    def show_frame(self, page_name: str):
        frame = self.frames[page_name]
        frame.tkraise()




if __name__ == "__main__":
    app = main()
    app.mainloop()
