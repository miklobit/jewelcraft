# ##### BEGIN GPL LICENSE BLOCK #####
#
#  JewelCraft jewelry design toolkit for Blender.
#  Copyright (C) 2015-2019  Mikhail Rachinskiy
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####


dictionary = {
    "*": {
        # Interface
        "Asset Manager": "Navigateur de ressources",
        "Asset name from active object": "Nom de ressource de l'objet actif",
        "Display asset name": "Affiche le nom de la Ressource",
        "Product Report": "Rapport de produit",
        "Report Language": "Langue du rapport",
        "Display in a new window": "Affiche dans une nouvelle fenêtre",
        "Save to file": "Enregistre le fichier",
        "Use custom library folder": "Utiliser un dossier de librairie personnel",
        "Gems": "Pierres précieuses",
        "Assets": "Ressources",
        "Select Gems By...": "Sélectionner les pierres par...",
        "Jeweling": "Bijoux",
        "Weighting": "Pondération",
        "Weighting Set": "Theme de pondérations",
        "Hide default sets": "Hide default sets",
        "[JewelCraft] Precious": "[Joaillerie] Précieux",
        "[JewelCraft] Precious RU (ГОСТ 30649-99)": "[Joaillerie] Précieux RU (ГОСТ 30649-99)",
        "[JewelCraft] Base": "[Joaillerie] Base",
        "Sizes": "Tailles",
        "Prongs": "Fourches",
        "Cutter": "Couteaux",
        "Library Folder Path": "Chemin du dossier de librairie",
        "Widgets": "Widgets",
        "Selection only": "Sélection seulement",
        "Use overrides": "Utiliser des substitutions",
        "Overrides only": "Substitutions seulement",
        "Widget Color": "Couleur du widget",
        "Line Width": "Epaisseur de ligne",
        "Show composition": "Afficher la composition",
        "Show density": "Afficher la densité",
        "Materials list": "Liste de matériaux",
        "Composition": "Composition",
        "Warnings": "Avertissements",
        "Hidden gems": "Cacher les pierres",
        # Popup dialogs
        "Asset Name": "Nom de ressources",
        "Category Name": "Nom des catégories",
        "Set Name": "Donner le nom",
        "Curvature Scale": "Echelle de la courbe",
        # Operator redo
        "Use Automated Presets": "Utiliser des réglages automatiques",
        "Prong Number": "Nombre de broche",
        "Detalization": "Detalization",
        "Intersection": "Intersection",
        "Bump Scale": "Echelle de relief",
        "Diameter": "Diamètre",
        "Size Offset": "Decalage de taille",
        "Girdle": "Ceinture",
        "Hole": "Trou",
        "Culet": "Culet",
        "Handle": "Poignée",
        "Curve Seat": "Siège courbe",
        "Curve Profile": "Profil courbe",
        "Bevel Corners": "Coins biseautés",
        "Length Offset": "Décalage de longueur",
        "Width Offset": "Décalage de largueur",
        "Position Offset": "Décalage de position",
        "Start Up": "Démarrage",
        "Mirror Axis": "Axe du miroir",
        "Select Children": "Sélectionner l'enfant",
        "Parent to selected": "Parent vers sélection",
        # Tooltips
        "Add gemstone to the scene": "Ajouter des pierres précieuses à la scène",
        "Edit selected gems": "Editer les pierres sélectionnées",

        "Commonly used precious alloys, physical properties taken directly from suppliers":
            "Alliages précieux couramment utilisés, propriétés physiques directement auprès des fournisseurs",

        "Set of precious alloys according to Russian regulations": "Ensemble d'alliages précieux selon la réglementation russe",

        "Set of base metal alloys, physical properties taken directly from suppliers":
            "Ensemble d'alliages de métaux communs, propriétés physiques directement auprès des fournisseurs",

        "Display product report in new window": "Afficher le rapport du produit dans une nouvelle fenêtre",
        "Save product report to file in project folder": "Enregistrer le rapport de produit dans un fichier dans le dossier du projet",
        "Product report language": "Langue du rapport du produit",
        "Use user preferences language setting": "Utiliser les paramètres de langue des préférences utilisateur",
        "Object for ring inner diameter reference": "Objet pour référence de diamètre intérieur de bague",
        "Object for shank width and height reference": "Objet pour référence de largeur et hauteur de tige",
        "Object for dimensions reference": "Objet pour référence de dimensions",
        "Object for weight reference": "Objet pour référence de poids",
        "Save product report to text file": "Enregistrer le rapport du produit dans un fichier texte",
        "Select gems by trait": "Sélectionnez des pierres par trait",

        "Select duplicated gems (located in the same spot)":
            "Sélectionnez les pierres dupliquées (situées au même endroit)",

        "Search stone by name": "Chercher les pierres par nom",
        "Search asset by name": "Chercher les ressources par nom",
        "Scatter selected object along active curve": "Distribuer l'objet sélectionné le long de la courbe active",
        "Redistribute selected objects along curve": "Redistribuer les objets sélectionnés le long de la courbe",

        "Display weight and volume for selected mesh objects":
            "Afficher le poids et le volume pour les objets de maillage sélectionnés",

        "Create dupli-face for selected objects": "Créer une dupli-face pour les objets sélectionnés",
        "Create size curve": "Créer une courbe de taille",

        (
            "Stretch deformed objects along curve on X axis, "
            "also works in Edit Mode with selected vertices"
        ): (
            "Étirer les objets déformés le long de la courbe sur l’axe X, "
            "fonctionne également en mode édition avec les sommets sélectionnés"
        ),

        "Display curve length": "Longueur de la courbe d'affichage",

        "Move deformed object over or under the curve":
            "Déplacer un objet déformé sur ou sous la courbe",

        "Mirror selected objects around one or more axes, keeping object data linked":
            "Mettre en miroir les objets sélectionnés autour d'un ou plusieurs axes, en maintenant les données d'objets liées",

        "Project selected objects onto active object using Lattice":
            "Projeter des objets sélectionnés sur un objet actif à l'aide de Lattice",

        "Deform active object profile with Lattice":
            "Déformer le profil d'objet actif avec Lattice",

        "Use automatically generated presets, discards user edits or presets":
            "Utiliser les préréglages générés automatiquement, ignorer les modifications utilisateur ou les préréglages",

        "Create prongs for selected gems": "Créer des griffes pour les pierres sélectionnées",
        "Create cutter for selected gems": "Créer une coupe pour les pierres sélectionnées",
        "Make curve start at the top": "Faire que la courbe commence en haut",
        "Density g/cm³": "Densité g/cm³",
        "Set of materials for weighting": "Ensemble de matériaux pour la pondération",
        "Create category": "Créer une catégorie",
        "Rename category": "Renommer une catégorie",
        "Refresh asset UI": "Rafraichir le menu des ressources",
        "Add selected objects to asset library": "Ajouter des objets sélectionnés à la bibliothèque d'actifs",
        "Rename asset": "Renommer la ressource",
        "Remove asset from library": "Renommer la ressource de la librairie",
        "Replace current asset with selected objects": "Remplacer la ressource avec les objets sélectionnés",
        "Replace asset preview image": "Remplacer la vignette de la ressource",
        "Import selected asset": "Importer la ressource sélectionnés",
        "Asset category": "Catégorie de la ressource",

        "Set custom asset library folder, if disabled the default library folder will be used": (
            "Définir le dossier de la bibliothèque d’actives personnalisée; le cas échéant, "
            "le dossier de la bibliothèque par défaut sera utilisé"
        ),

        "Custom library folder path": "Chemin du dossier de la bibliothèque personnalisée",
        "Display asset name in Tool Shelf": "Display asset name in Tool Shelf",

        "Use active object name when creating new asset":
            "Utiliser le nom de l'objet actif pour la création d'une nouvelle ressource",

        "Enable widgets drawing": "Activer le dessin des widgets",
        "Draw widgets only for selected objects": "Dessiner des widgets uniquement pour les objets sélectionnés",
        "Use object defined widget overrides": "Utiliser les substitutions de widget définis par un objet",

        "Display only object defined widget overrides":
            "Afficher uniquement les substitutions de widget définies par un objet",

        "Draw widgets in front of objects": "Dessiner des widgets devant des objets",

        "Override widget display properties for selected objects":
            "Substituer les propriétés d'affichage du widget pour les objets sélectionnés",

        "Remove widget override properties from selected objects":
            "Supprimer les propriétés de substitution de widget des objets sélectionnés",

        "Add new material to the list": "Ajouter un nouveau matériau à la liste",
        "Remove material from the list": "Supprimer le matériau de la liste",
        "Display material density in the list": "Afficher la densité de matière dans la liste",
        "Display material composition in the list": "Afficher la composition du matériau dans la liste",
        "Create weighting set from materials list": "Créer un jeu de pondération à partir de la liste des matériaux",
        "Remove weighting set": "Retirer le jeu de pondération",
        "Rename weighting set": "Renommer le jeu de pondération",

        "Load weighting set to the materials list by replacing existing materials":
            "Charger la pondération définie dans la liste des matériaux en remplaçant les matériaux existants",

        "Append weighting set at the end of the current materials list":
            "Ajouter la pondération définie à la fin de la liste des matières en cours",

        "Hide default JewelCraft sets from weighting sets menu":
            "Masquer les jeux de bijoux par défaut dans le menu des ensembles de pondération",

        "Replace selected weighting set with current materials list":
            "Remplacer le jeu de pondération sélectionné par la liste des matériaux en cours",

        "Material name": "Nom de materiau",
        "Material composition": "Composition du matériau",

        "Use one-dimensional lattice for even deformation":
            "Utilisez un réseau d'une dimension pour une déformation uniforme",

        "Use two-dimensional lattice for proportional deformation":
            "Utiliser un lattice pour la déformation proportionnelle",

        "Scale selected objects to given size": "Échelle des objets sélectionnés à une taille donnée",
        "Move each object individually": "Move each object individually",

        "Enable material for weighting and product report":
            "Activer le matériau pour la pondération et le rapport de produit",

        "Clear materials list": "Effacer la liste des matériaux",

        "Show warning if there are hidden gem objects in the scene":
            "Afficher un avertissement s'il y a des objets cachés dans la scène",

        "Parent imported asset to selected objects (Shortcut: hold Alt when using the tool)": (
            "Parenter la ressource importée pour les objets sélectionnés "
            "(Raccourcie: Alt en utilisant l'outil)"
        ),
        # Reports
        "WARNING": "AVERTISSEMENT",
        "Possible gem dupli-face leftovers": "Restes de pierres dupli-face possibles",
        "Hidden gems (use Show Hidden/Alt H)": "Cacher les pierres (utiliser Afficher/Cacher: Alt + H)",
        "Duplicated gems": "Pierres dupliquées",

        "Deprecated gem IDs (use Convert Deprecated Gem IDs from Operator Search menu)":
            "ID de pierre obsolète (utiliser Convert Deprecated Gem IDs dans le menu de recherche de fonction)",

        "Unknown gem IDs, carats are not calculated for marked gems (*)":
            "IDs de pierre inconnus, les carats sont calculés pour des pierres marquées (*)",

        "Curve Length": "Longueur de la courbe",
        "{} duplicates found": "{} duplications trouvées",

        "Text file successfully created in the project folder":
            "Fichier texte créé avec succès dans le dossier du projet",

        "Could not create text file, project folder does not exist":
            "Impossible de créer un fichier texte, le dossier du projet n'existe pas",

        "At least two objects must be selected": "Au moins deux objets doivent être sélectionnés",
        "At least one gem object must be selected": "Au moins une pierre doit être sélectionnée",
        "At least one mesh object must be selected": "Au moins un mesh doit être sélectionné",
        "Active object must be a curve": "L'objet actif doit être une courbe",

        "Selected objects do not have Follow Path constraint":
            "Les objets sélectionnés n'ont pas de contrainte de suivi de chemin",

        "File not found": "Fichier non trouvé",
        "Name must be specified": "Le nom doit être spécifié",
        # Cuts
        "Round": "Rond",
        "Oval": "Ovale",
        "Cushion": "Coussin",
        "Pear": "Poire",
        "Marquise": "Marquise",
        "Princess": "Princesse",
        "Baguette": "Baguette",
        "Square": "Carré",
        "Asscher": "Asscher",
        "Radiant": "Radiant",
        "Flanders": "Flamands",
        "Octagon": "Octaèdre",
        "Heart": "Coeur",
        "Trillion": "Billion",
        "Trilliant": "Trilliant",
        "Triangle": "Triangle",
        # Stones
        "Alexandrite": "Alexandrite",
        "Amethyst": "Amethyste",
        "Aquamarine": "Aquamarine",
        "Citrine": "Citrine",
        "Cubic Zirconia": "Zircone cubique",
        "Diamond": "Diamand",
        "Emerald": "Emeraude",
        "Garnet": "Grenat",
        "Morganite": "Morganite",
        "Peridot": "Péridot",
        "Quartz": "Quartz",
        "Ruby": "Rubis",
        "Sapphire": "Saphir",
        "Spinel": "Spinelle",
        "Tanzanite": "Tanzanite",
        "Topaz": "Topaze",
        "Tourmaline": "Tourmaline",
        "Zircon": "Zircon",
        # Alloys
        "Yellow Gold 24K": "Or Jaune 24K",
        "Yellow Gold 22K": "Or Jaune 22K",
        "Yellow Gold 18K": "Or Jaune 18K",
        "Yellow Gold 14K": "Or Jaune 14K",
        "Yellow Gold 10K": "Or Jaune 10K",
        "White Gold 18K Pd": "Or blanc 18K Pd",
        "White Gold 18K Ni": "Or blanc 18K Ni",
        "White Gold 14K Pd": "Or blanc 14K Pd",
        "White Gold 14K Ni": "Or blanc 14K Ni",
        "White Gold 10K": "Or blanc 10K",
        "Rose Gold 18K": "Or rose 18K",
        "Rose Gold 14K": "Or rose 14K",
        "Rose Gold 10K": "Or rose 10K",
        "Yellow Gold 999": "Or Jaune 999",
        "Yellow Gold 958": "Or Jaune 958",
        "Yellow Gold 750": "Or Jaune 750",
        "Yellow Gold 585": "Or Jaune 585",
        "Yellow Gold 375": "Or Jaune 375",
        "White Gold 750 Pd": "Or blanc 750 Pd",
        "White Gold 750 Ni": "Or blanc 750 Ni",
        "White Gold 585 Pd": "Or blanc 585 Pd",
        "White Gold 585 Ni": "Or blanc 585 Ni",
        "Red Gold 585": "Or rouge 585",
        "Red Gold 375": "Or rouge 375",
        "Platinum 950": "Platine 950",
        "Platinum 900": "Platine 900",
        "Palladium 950": "Palladium 950",
        "Silver 925": "Argent 925",
        "Silver Sterling": "Argent Sterling",
        "Brass": "Laiton",
        "Bronze": "Bronze",
        "Steel Stainless": "Acier inoxydable",
        "Titanium": "Titane",
        # Product report
        "Size": "Taille",
        "Shank": "Jarret",
        "Dimensions": "Dimensions",
        "Weight": "Poid",
        "Volume": "Volume",
        "Settings": "Réglages",
        "Gem": "Pierre",
        "Cut": "Coupe",
        "Qty": "Qté",
        # Units
        "pcs": "pcs",
        "mm": "mm",
        "mm³": "mm³",
        "g": "g",
        "ct.": "ct.",
    },
    "JewelCraft": {
        "Cut": "Coupe",
        "Dimensions": "Dimensions",
        "Round": "Arrondi",
    },
    "Dative": {
        "Size": "Taille",
        "Stone": "Pierre",
        "Cut": "Coupe",
    },
    "Operator": {
        "Add Gem": "Ajouter une pierre",
        "Doubles": "Doubles",
        "Curve Scatter": "Dispersion de la courbe",
        "Prongs": "Fourches",
        "Cutter": "Couteau",
        "Make Dupli-face": "Créer un dupli-face",
        "Lattice Project": "Projet de lattice",
        "Lattice Profile": "Profil de lattice",
        "Size Curve": "Courbe de taille",
        "Stretch": "Étendue",
        "Curve Length": "Longueur de la courbe",
        "Product Report": "Rapport de produit",
        "Open Library Folder": "Ouvrir le dossier de la librairie",
        "Import Asset": "Importer la ressource",
        "Rename": "Renommer",
        "Replace Asset": "Remplacer la ressource",
        "Replace Preview": "Remplacer la vignette",
        "Create Category": "Créer une catégorie",
        "Rename Category": "Créer une catégorie",
        "Rename Asset": "Renommer la ressource",
        "Remove Asset": "Remplacer la ressource",
        "Replace Asset Preview": "Remplacer la vignette de la ressource",
        "Override": "Outrepasser",
        "Clear List": "Effacer la liste",
        "Add New Material": "Ajouter un nouveau matériau",
        "Create Set": "Créer un jeu",
        "Replace Set": "Remplacer un jeu",
        "Remove Set": "Effacer un jeu",
        "Rename Set": "Renommer un jeu",
    },
}
