import cv2

planetas = cv2.imread("solar-system.jpg")

cv2.putText(planetas,
            "Sol",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
             )

cv2.putText(planetas,
            "Mercurio",
            (120,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
             )

cv2.putText(planetas,
            "Venus",
            (200,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
             )

cv2.putText(planetas,
            "Tierra",
            (300,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
             )

cv2.putText(planetas,
            "marte",
            (380,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
             )


cv2.putText(planetas,
            "Jupiter",
            (550,70),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
             )

cv2.putText(planetas,
            "Saturno",
            (750,110),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
             )

cv2.putText(planetas,
            "Urano",
            (970,140),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
             )

cv2.putText(planetas,
            "Neptuno",
            (1150,150),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
             )











cv2.imshow("los Planetas", planetas)



cv2.waitKey(0)