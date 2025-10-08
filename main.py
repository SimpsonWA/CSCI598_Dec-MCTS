from manim import *
from manim_slides import Slide
from PIL import Image
import copy

def GrowSearchTree():
            group = VGroup()
            title = Tex(r"Grow Search Tree")
            group.add(title)
            vertices = [0, 1, 2, 3, 4, 5, 6]

            # Define edges (connections between nodes)
            edges = [
                (0, 1), (0, 2),  # root -> children
                (1, 3), (1, 4),  # left child -> grandchildren
                (2, 5), (2, 6)   # right child -> grandchildren
            ]

            # Create graph
            tree = Graph(
                vertices,
                edges,
                layout="tree",              # use tree layout
                layout_scale=1,
                root_vertex=0,  # root node
                vertex_config={"radius": 0.1, "fill_color": BLUE},
                edge_config={"stroke_color": WHITE}
            )
            group.add(tree)
            group.arrange(DOWN)  # arrange after adding
            box = SurroundingRectangle(group, color = WHITE, buff = MED_LARGE_BUFF)
            group.add(box)
            return group
def OptimizeActions():
       group = VGroup()
       text = MarkupText(
            "Optimize Action\nSequence Probabilities",
            color=WHITE,
        ).scale(0.5)
       group.add(text)
       # Need to add dummy chart
       group.arrange(DOWN)  # arrange after adding
       box = SurroundingRectangle(group, color = WHITE, buff = MED_LARGE_BUFF)
       group.add(box)
       return group

def CommPlans():
    group = Group()

    # Title
    title = MarkupText("Communication Plan", color=WHITE).scale(0.5)

    # WiFi icons
    wifi_icon = ImageMobject("Wifi_fixed.png").scale(0.75)
    wifi_1 = wifi_icon.copy()
    wifi_2 = wifi_icon.copy()

    # Labels under each icon
    label1 = Text("Robot r", font_size=24).next_to(wifi_1, DOWN)
    label2 = Text("Robot r′", font_size=24).next_to(wifi_2, DOWN)

    # Place the icons side by side
    icon_group = Group(
        Group(wifi_1, label1),
        Group(wifi_2, label2)
    ).arrange(RIGHT, buff=2)

    # Arrows back and forth
    arrow1 = Arrow(
        start=wifi_1.get_right(), 
        end=wifi_2.get_left(),
        buff=0.2, color=YELLOW
    )
    arrow2 = Arrow(
        start=wifi_2.get_left(), 
        end=wifi_1.get_right(),
        buff=0.2, color=YELLOW
    )

    # Combine everything
    group.add(title, icon_group, arrow1, arrow2)

    # Box around
    box = SurroundingRectangle(group, color=WHITE, buff=MED_LARGE_BUFF)
    group.add(box)

    return group


class Contributions_Gap(Slide):
    def construct(self):
        frame_width = self.camera.frame_width
        frame_height = self.camera.frame_height
        title = Tex("Gap").scale(1.25).to_corner(UP)
        self.play(FadeIn(title, shift = UP))
        self.wait(0.02)
        self.next_slide()


class Related_Work(Slide):
    def show_title(self, text, prev_title=None):
        """Helper function to animate title transitions."""
        new_title = Tex(text).scale(1.25).to_corner(UP)
        if prev_title:
            self.play(FadeOut(prev_title, shift=UP),
                      FadeIn(new_title, shift=UP))
        else:
            self.play(FadeIn(new_title, shift=UP))
        self.next_slide()
        return new_title

    def construct(self):
        frame_width = self.camera.frame_width
        frame_height = self.camera.frame_height

        title_1 = self.show_title("Related Work - Decentralized Information Gathering")
        # Blah 

        title_2 = self.show_title("Related Work - Dec-POMDPs", prev_title=title_1)
        # Blah 

        title_3 = self.show_title("Related Work - MCTS", prev_title=title_2)
        # Blah 

        title_4 = self.show_title("Related Work - Variational Methods for Planning", prev_title=title_3)
        # Blah 

        title_5 = self.show_title("Related Work - Non-myopic, Single Robot Planning", prev_title=title_4)
        # Blah 


class Overview(Slide):
    def construct(self):
        
        frame_width = self.camera.frame_width
        frame_height = self.camera.frame_height

        title = Tex("Overview of DEC-MCTS for Robot r").scale(1.25).to_corner(UP)
        self.play(FadeIn(title, shift = DOWN))
        self.next_slide()

        algo_template = TexTemplate()
        
        # Add the algorithm2e package to the preamble
        algo_template.add_to_preamble(r"\usepackage[ruled]{algorithm2e}")
        algo_code = r"""
        \begin{algorithm}[H]
        \caption{Overview of Dec-MCTS for robot $r$}
        \KwIn{Global objective function $g$, budget $B_r$, feasible action sequences and costs}
        \KwOut{Sequence of actions $x_r$ for robot $r$}

        $T_r \gets$ initialize MCTS tree\;

        \While{\text{computation budget not met, at iteration} $n$}{

            $\hat{X}_n^r \gets \text{SELECT\_SET\_OF\_SEQUENCES}(T_r)$ 

            \For{$i = 1$ \KwTo $\tau_n$}{
                $T_r \gets \text{GROW\_TREE}(T_r, \hat{X}_n^r, q_n^r, B_r)$ 

                $q_n^r \gets \text{UPDATE\_DISTRIBUTION}(\hat{X}_n^r, q_n^r, \beta)$

                $\text{COMMUNICATION\_TRANSMIT}(\hat{X}_n^r, q_n^r)$ 

                $(\hat{X}_n^r, q_n^r) \gets \text{COMMUNICATION\_RECEIVE}()$ 

                $\beta \gets \text{COOL}(\beta)$ 
            }
        }
        \Return $x_r \gets \arg\max_{x_r \in \hat{X}_n^r} q_n^r(x_r)$\;

        \end{algorithm}
        """

        algo_mobject = Tex(algo_code, tex_template=algo_template, font_size=28)
        self.play(FadeIn(algo_mobject, shift = UP))
        self.next_slide()

class MCTS_Simple(Slide):
    def construct(self):
        # === TITLE ===
        title = Tex("Simple MCTS").scale(1.25)
        title.to_corner(UP)
        self.play(FadeIn(title, shift=UP))
        self.next_slide()

        # === GRAPH STRUCTURE ===
        nodes = list(range(15))
        edges = [
            (0, 1), (0, 2), (0, 3),
            (1, 4), (1, 5), (1, 6),
            (2, 7), (2, 8), (2, 9),
            (3, 10), (3, 11), (3, 12),
            (12, 13), (12, 14)
        ]

        graph = Graph(
            nodes,
            edges,
            layout="tree",
            root_vertex=0,
            layout_scale=6,
            vertex_config={"radius": 0.3, "color": BLUE},
            edge_config={"stroke_color": GRAY}
        )

        graph.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(graph, shift=UP))
        self.next_slide()

        # === PHASE LABEL SETUP ===
        phase_title = Tex(r"\textbf{Phase: }").scale(1.5).next_to(graph, DOWN, buff = 2)
        phase_label = Tex("").next_to(phase_title, RIGHT)
        self.play(Write(phase_title), FadeIn(phase_label))
        self.next_slide()

        # === PHASE 1: SELECTION ===
        selection_color = YELLOW
        selection_path = [0, 3, 12, 14]
        self.play(Transform(phase_label, Tex("Selection", color=selection_color).scale(1.5).next_to(phase_title, RIGHT)))

        selection_arrows = VGroup()
        for i in range(len(selection_path) - 1):
            start = graph[selection_path[i]].get_center()
            end = graph[selection_path[i+1]].get_center()
            arrow = Arrow(start=start, end=end, buff=0.1, color=selection_color)
            selection_arrows.add(arrow)
        self.play(LaggedStartMap(Create, selection_arrows, lag_ratio=0.3))
        self.next_slide()

        # === PHASE 2: EXPANSION ===
        expansion_color = GREEN
        self.play(Transform(phase_label, Tex("Expansion", color=expansion_color).scale(1.5).next_to(phase_title, RIGHT)))
        new_node = 15
        parent_node = 14
        new_node_dot = Dot(graph[parent_node].get_center(), color=expansion_color, radius=0.3).next_to(
             graph[parent_node].get_center(), DOWN, buff = 0.75
        )
        edge = Line(graph[parent_node].get_center(), new_node_dot.get_center(), color=expansion_color)
        self.play(Create(edge), FadeIn(new_node_dot, scale=0.5))
        self.play(FadeOut(selection_arrows))
        self.next_slide()

        # === PHASE 3: SIMULATION ===
        simulation_color = ORANGE
        self.play(Transform(phase_label, Tex("Simulation", color=simulation_color).scale(1.5).next_to(phase_title, RIGHT)))
        sim_arrow = DashedLine(new_node_dot.get_center(), new_node_dot.get_center() + DOWN*1.5, color=simulation_color)
        sim_label = Tex("Simulate rollout").scale(0.8).next_to(sim_arrow, DOWN)
        self.play(Create(sim_arrow), FadeIn(sim_label))
        self.next_slide()

        # === PHASE 4: BACKPROPAGATION ===
        backprop_color = RED
        self.play(Transform(phase_label, Tex("Backpropagation", color=backprop_color).scale(1.5).next_to(phase_title, RIGHT)))

        backprop_arrows = VGroup()
        for i in reversed(range(len(selection_path))):
            start = graph[selection_path[i]].get_center()
            end = graph[selection_path[i-1]].get_center() if i > 0 else graph[0].get_center()
            arrow = Arrow(start=start, end=end, buff=0.1, color=backprop_color)
            backprop_arrows.add(arrow)
        self.play(LaggedStartMap(Create, backprop_arrows, lag_ratio=0.3))

        # Cleanup / Fade out
        self.play(FadeOut(VGroup(phase_label, phase_title, sim_label, sim_arrow, new_node_dot, edge, backprop_arrows)), FadeOut(graph), FadeOut(title))

        
class MCTS_DUCB(Slide):
     def construct(self):
        title = Tex("MCTS with D-UCB Selection").scale(1.25).to_corner(UP)
        self.play(FadeIn(title,shift = DOWN))
        self.next_slide()
            # Create the Algo
        algo_template = TexTemplate()
            # Add the algorithm2e package to the preamble
        algo_template.add_to_preamble(r"\usepackage[ruled]{algorithm2e}")
        algo_code = r"""
            \begin{algorithm}[H]
            \caption{Grow the search tree for robot $r$ using MCTS}
            \KwIn{Partial tree $\mathcal{T}^r$, distributions for other robots $(\hat{\mathcal{X}}_n^{(r)}, q_n^{(r)})$, budget $B^r$}
            \KwOut{updated partial tree $\mathcal{T}^r$}

            \For{fixed number of samples }{
                    $i_{d-1} \gets NODESELECTIOND-UCT(\mathcal{T}^r)$\;

                    $i_d \gets EXPANDTREE(i_{d-1})$\;

                    $\bold{x}^{(r)} \gets SAMPLE(\hat{\mathcal{X}}_n^{(r)}, q_n^{(r)})$\;

                    $\bold{x}^{r} \gets PERFORMROLLOUTPOLICY(i_d , \bold{x}^{(r)}, B^r)$\;

                    $F_t \gets f^r(\bold{x}^r \cup \bold{x}^{(r)})$\;

                    $\mathcal{T}^r \gets BACKPROPAGATION(\mathcal{T}^r, i_d , F_t)$\;
                
            }
            \Return $\mathcal{T}^r$\;

            \end{algorithm}
            """

        algo_mobject = Tex(algo_code, tex_template=algo_template, font_size=32)
        self.play(FadeIn(algo_mobject))
        self.next_slide()


            # Now show the arg max for selecting node with the highest UCB Score 
        algo_template = TexTemplate()
        
            #Add the asmath
        algo_template.add_to_preamble(r"\usepackage{amsmath}")

        arg_max_UCB = MathTex(r" I_{i_{d}, t}",
                            r" = \operatorname*{argmax}_{j \in C(i_d)} U_{j,t_{i_d},t_j} ").scale(1.25)

        self.play(FadeIn(arg_max_UCB, shift = UP))
        self.next_slide()

            # Underline I to emphasize what this actually is 
        underline_I = Underline(arg_max_UCB[0], color = YELLOW)
        self.play(Create(underline_I))
        self.next_slide()

        self.play(FadeOut(underline_I, shift = LEFT),
                      FadeOut(arg_max_UCB, shift = LEFT))
            
            # Swap the Selection node equation with the UCB equation 
        D_UCB_eq = MathTex(
            r"U_{j,t_{i_d},t_j}(\gamma) = \hat{F}_{j,t_j}(\gamma) + c_{t_{i_d}, t_j}(\gamma)"
            ).scale(1.25)
        D_UCB_eq.move_to(arg_max_UCB.get_center())
        self.play(FadeIn(D_UCB_eq, shift = RIGHT))
        self.next_slide()


            # Create gamma TODO(SMW): Cleanup the positioning  
        gamma = MathTex(r"\gamma \in (\frac{1}{2}, 1) \text{: Discount Factor}").next_to(D_UCB_eq, DOWN, buff  = 0.25)
        self.play(Create(gamma))
        self.next_slide()

            # Child node with discount factor
        child_node_count = MathTex(r"t_j(\gamma) = \sum_{u=1}^{t} \gamma^{t-u} \bold{1}_{(I_{i_d},u=j)} \text{: Discounted num. of times child node visited}").next_to(gamma,DOWN,buff = 0.25)
        self.play(Create(child_node_count))
        self.next_slide()
            
            # Parent node visited 
        parent_node_count = MathTex(r"t_{i_d}(\gamma) = \sum_{j \in C(i_d)} t_j(\gamma) \text{: Discounted num. of times Parent node visited}").next_to(child_node_count,DOWN,buff = 0.25)
        self.play(Create(parent_node_count))
        self.next_slide()
      
            # Discounted Emperical Average: 
        dis_empircal_avg = MathTex(r"\hat{F}_{j,t_j}(\gamma) = \frac{1}{t_{j}(\gamma)} \sum_{u=1}^{t} \gamma^{t-u}F_{u}  \bold{1}_{(I_{i_d},u=j)}").next_to(parent_node_count,DOWN,buff = 0.25) 
        self.play(Create(dis_empircal_avg))
        self.next_slide()

            # Discounted Exploration Bonus: 
        dis_exp_bonus = MathTex(r"c_{t_{i_d}, t_j}(\gamma) := 2C_p \sqrt{\frac{\log t_{i_d}(\gamma)}{t_j(\gamma)}}").next_to(dis_empircal_avg,DOWN,buff = 0.25) 
        self.play(Create(dis_exp_bonus))
        self.next_slide()
