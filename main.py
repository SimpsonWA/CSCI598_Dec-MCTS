from manim import *
from manim_slides import Slide
from PIL import Image
import copy

myTemplate = TexTemplate()
myTemplate.add_to_preamble(r"\usepackage[ruled]{algorithm2e}")
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
            title = Tex("MCTS with D-UCB").scale(1.25).to_corner(UP)
            self.play(FadeIn(title,shift = DOWN))
            self.wait(0.01)
            self.next_slide()
      
        
