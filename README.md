# Team Ijwit

**Hattum Smit**
**Miro Zwering**
**Jeroen Reemer**  
 
**Programmeertheorie**
**Protein Po(w)der**

**©2020 Alle rechten voorbehouden**

Algoritmes om de beste vouwing te vinden van eiwitten.

## Case introductie
Eiwitten zijn lange ketens van aminozuren. De vouwing van deze aminozuren vormt de basis van de werking van de eiwitten. Verkeerd gevouwen eiwitten kunnen aan de basis staan van onder andere ziektes zoals kanker en alzheimer. De wetenschap en farmaceutische industrie zijn er dus bij gebaat om te weten wat de effecten van bepaalde vwouwing zijn.

Voor deze case gaan we op zoek naar de meest stabiele vouwing voor een vast staand aantal eiwitten, namelijk:
* 0: HHPHHHPH
* 1: HHPHHHPHPHHHPH
* 2: HPHPPHHPHPPHPHHPPHPH
* 3: PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP
* 4: HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH
* 5: PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP
* 6: CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC
* 7: HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH
* 8: HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH

Wat de beste vouwing is wordt bepaald aan de hand van een bepaald puntenschema. Om een versimpelde voorstelling van de realiteit te kunnen maken worden er een paar aannames gemaakt:
* 1: Eiwitten worden gevouwen op een 2D grid. Verbindingen tussen aminozuren kunnen alleen recht zijn of een hoek van 90 graden maken.
* 2: Er zijn 3 soorten aminozuren: Hydrofoob, Polair & Cysteine. De score die wordt toegekend aan een bepaalde binding is: H - H = -1, P - P = 0, H - C = -1, C - C = -5. Hoe lager de score, hoe stabieler het eiwit!
* Verbindingen in de amino-keten zelf tellen niet mee in de score.

Voorbeeld: 
![voorbeeld](voorbeeld.JPG)

## Algoritmes
In totaal kunnen er 4 verschillende algoritmes toegepast worden om een beste vouwing te vinden:
* **Random:** Voor elk volgend aminozuur in de eiwitketen wordt een compleet willekeurige vouwing gekozen, rekening houdend met het feit dat vouwingen niet kruizen
* **Cyclefold:** Het eiwit wordt als een spiraal om zijn eigen as gevouwen.
* **Priority:**
* **Greedy with look ahead:** Kijkt een gegeven aantal stappen vooruit en berekent van al die uitkomsten de beste score. De eerst volgende beste stap wordt dan uitgevoerd waarna vervolgens het zelfde proces wordt herhaald. Er wordt lokaal steeds een optimale keuze gemaakt.

# File Navigatie
Alle algoritmes kunnen worden aangeroepen door main.py te runnen. Vervolgens wordt je door middel van vragen in de terminal door een keuzemenu heen genomen waar aangegeven kan worden welk algoritme je wilt gebruiken, en welke eventuele diepte(look ahead) je wilt meegeven.

De stabielst gevonden manier om het eiwit te vouwen wordt uiteindelijk geplot in een Visualisation.png bestand. De stapsgewijze vouwingen kunnen worden ingekeken in Visualisation.csv.
