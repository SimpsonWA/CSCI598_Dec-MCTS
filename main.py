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

        # The LaTeX code for the algorithm
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


class MCTS(Slide):
      def construct(self):
            title = Tex("MCTS with D-UCB Selection").scale(1.25).to_corner(UP)
            self.play(FadeIn(title,shift = DOWN))
            self.next_slide()
            nodes1 = [0, 
                      1, 2, 3,
                      4, 5, 6,
                      7, 8, 9, 
                      10, 11, 12]
            edges1 = [(0, 1), (0, 2), (0, 3),
                      (1, 4), (1, 5), (1, 6),
                      (2, 7), (2, 8), (2, 9),
                      (3, 10), (3, 11), (3, 12)
                      ]

            # Create Graph object but don't show it yet
            graph1 = Graph(
                nodes1,
                edges1,
                layout="tree",  # nice tree layout
                root_vertex= 0,
                layout_scale=6,
                vertex_config={"radius": 0.3, "color": BLUE},
                edge_config={"stroke_color": WHITE}
            )
            # Create inital graph and ask well how do we select a node to traverse??? 
            graph1.next_to(title,DOWN, buff = 0.5)
            self.play(FadeIn(graph1, shift = UP))
            self.next_slide()


            # Create arrows through different paths
            path1 = [0, 1, 4]   #
            path2 = [0, 2, 9]  
            arrow_groups1 = VGroup()
            # Animate traversal of first path
            for i in range(len(path1) - 1):
                start = graph1[path1[i]].get_center()
                end = graph1[path1[i+1]].get_center()
                arrow = Arrow(
                     start = start,
                     end = end,
                     buff = 0.1,
                     color = YELLOW
                )
                self.play(Create(arrow))
                arrow_groups1.add(arrow)
            self.play(FadeOut(arrow_groups1))
            
            # Pause at leaf
            self.wait(0.1)

            arrow_groups2 = VGroup()
            # Animate traversal of first path
            for i in range(len(path2) - 1):
                start = graph1[path2[i]].get_center()
                end = graph1[path2[i+1]].get_center()
                arrow = Arrow(
                     start = start,
                     end = end,
                     buff = 0.1,
                     color = YELLOW
                )
                self.play(Create(arrow))
                arrow_groups2.add(arrow)
            self.play(FadeOut(arrow_groups2))
            # Pause at leaf
            self.wait(0.1)
            self.next_slide()

            # Now show the arg max for selecting node with the highest UCB Score 
            algo_template = TexTemplate()
        
            #Add the asmath
            algo_template.add_to_preamble(r"\usepackage{amsmath}")

            arg_max_UCB = MathTex(r" I_{i_{d}, t}",
                                  r" = \operatorname*{argmax}_{j \in C(i_d)} U_{j,t_{i_d},t_j} ").scale(1.25)
            arg_max_UCB.next_to(graph1, DOWN, buff = 1)

            self.play(FadeIn(arg_max_UCB, shift = UP))
            self.next_slide()

            # Underline I to emphasize what this actually is 
            underline_I = Underline(arg_max_UCB[0], color = YELLOW)
            self.play(Create(underline_I))
            self.next_slide()

            # Start from root and say its really just trying to find a node that has the maximum UCB  score
            root_copy = copy.deepcopy(graph1.vertices[0])
            root_copy.set_color(RED)
            self.play(FadeIn(root_copy))
            for _ in range(3):
                self.play(Indicate(graph1.vertices[1]),
                        Indicate(graph1.vertices[2]),
                        Indicate(graph1.vertices[3]))
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

            # Move around the Graph and UCB Equation 
            self.play(FadeOut(graph1,shift = LEFT),
                      FadeOut(root_copy),
                      D_UCB_eq.animate.next_to(title, DOWN, buff = 0.5))
            self.next_slide()

            # Create gamma TODO(SMW): Cleanup the positioning  
            gamma = MathTex(r"\gamma \in (\frac{1}{2}, 1) \text{: Discount Factor}")
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
