from manim import *

class Ex2_6(Scene):
    
    def construct(self):

        #Parâmetro com valor inicial para a evoluta ter algum ponto
        u = ValueTracker(0.01)
        
        #Eixos
        axes = Axes(
            x_range=[-7, 7, 1],
            x_length=14,
            y_range=[-7, 7, 1],
            y_length=14
        ).add_coordinates()

        #Círculo fixado
        r=1 #raio do círculo
        fcircle=Circle(radius=r,color=WHITE);
        
        # Evoluta
        evoluta = always_redraw(lambda: ParametricFunction(lambda t : axes.coords_to_point(r*(np.cos(t)+t*np.sin(t)),r*(np.sin(t)-t*np.cos(t))),t_range=[0,u.get_value()],color=BLUE))
        arco = always_redraw(lambda: ParametricFunction(lambda t : axes.coords_to_point(r*np.cos(t),r*np.sin(t)),t_range=[0,u.get_value()],color=YELLOW))

        #Pontos
        T = always_redraw(lambda : Dot(fill_color = GREEN, fill_opacity = 0.8).move_to(fcircle.point_at_angle(u.get_value())))
        Ttext = always_redraw(lambda : Tex("$T(\\theta)$", color = GREEN).next_to(T))
        P = always_redraw(lambda : Dot(fill_color = RED, fill_opacity = 0.8).move_to(evoluta.get_end()))
        Ptext = always_redraw(lambda : Tex("$P(\\theta)$", color = RED).next_to(P))
        
        #Linha de P a T meio porco, mas é o que dá
        def conecta_pontos():
            x = P.get_center()[0]
            y = P.get_center()[1]
            return Line(T.get_center(), np.array([x,y,0]), color=YELLOW)
        PtoT=always_redraw(conecta_pontos)

        # Animação
        rt = 3 #duração da animação
        self.play(LaggedStart(Create(axes), Create(fcircle), run_time=2))
        self.wait()
        self.add(evoluta)
        self.wait()
        self.add(T,Ttext,P,Ptext)
        self.add(arco)
        self.add(PtoT)
        self.play(u.animate.set_value(2*PI), run_time = rt, rate_func = linear)
        self.wait(3)

