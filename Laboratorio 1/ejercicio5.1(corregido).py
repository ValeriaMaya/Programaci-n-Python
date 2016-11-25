def seg(ss):
    if ss<60:
        segundos=ss
        print segundos,"segundo(s)"
    else:
        if ss<3600:
            if ss%60==0:
                minutos=ss/60
                print minutos,"minuto(s)"
            else:
                minutos=(ss/60)-(ss%60/60)
                print minutos,"minuto(s)"
                segundos=ss%60
                print segundos,"segundo(s)"
        else:
            if ss<86400:
                if ss%3600==0:
                    horas=ss/3600
                    print horas,"hora(s)"
                else:
                    horas=(ss/3600)-(ss%3600/3600)
                    print horas,"hora(s)"
                    if ss%3600<60:
                        segundos=ss%3600
                        print segundos,"segundo(s)"
                    else:
                        if (ss%3600)%60==0:
                            minutos=(ss%3600)/60
                            print minutos,"minuto(s)"
                        else:
                            minutos=((ss%3600)/60)-(((ss%3600)%60)/60)
                            print minutos,"minuto(s)"
                            segundos=(ss%3600)%60
                            print segundos,"segundo(s)"
            else:
                if ss%86400==0:
                    dias=ss/86400
                    print dias,"dia(s)"
                else:
                    dias=(ss/86400)-(ss%86400/86400)
                    print dias,"dia(s)"
                    if ss%86400<60:
                        segundos=ss%86400
                        print segundos,"segundo(s)"
                    else:
                        if ss%86400<3600:
                            if (ss%86400)%60==0:
                                minutos=(ss%86400)/60
                                print minutos,"minuto(s)"
                            else:
                                minutos=((ss%86400)/60)-(((ss%86400)%60)/60)
                                print minutos,"minuto(s)"
                                segundos=(ss%86400)%60
                                print segundos,"segundo(s)"
                        else:
                            if (ss%86400)%3600==0:
                                horas=(ss%86400)/3600
                                print horas,"hora(s)"
                            else:
                                horas=((ss%86400)/3600)-(((ss%86400)%3600)/3600)
                                print horas,"hora(s)"
                                if (ss%86400)%3600<60:
                                    segundos=(ss%86400)%3600
                                    print segundos,"segundo(s)"
                                else:
                                    if (ss%86400)%3600<3600:
                                        if ((ss%86400)%3600)%60==0:
                                            minutos=((ss%86400)%3600)/60
                                            print minutos,"minuto(s)"
                                        else:
                                            minutos=(((ss%86400)%3600)/60)-((((ss%86400)%3600)%60)/60)
                                            print minutos,"minuto(s)"
                                            segundos=((ss%86400)%3600)%60
                                            print segundos,"segundo(s)"
