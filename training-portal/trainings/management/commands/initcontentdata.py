from django.core.management.base import BaseCommand
from trainings.models import Content
from accounts.models import ContentCreator, SkillLevel


BEGINNER = SkillLevel.objects.get(pk=1)
INTERMEDIATE = SkillLevel.objects.get(pk=2)
ADVANCE = SkillLevel.objects.get(pk=3)

CONTENT_CREATOR = ContentCreator.objects.first()

class Command(BaseCommand):
    help = "Intialize content data from ARSET"
    
    def handle(self, *args, **options):
        content = Content.objects.create(
        title="A Q&A Session on Radar Remote Sensing",
        description="A Q&A Session on Radar Remote Sensing",
        skill_level= BEGINNER,
        date= "2022-08-23 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-evaluating-ecosystem-services-remote-sensing",
        creator=CONTENT_CREATOR
        ) 
        content.thematic_area.add(*tuple("Agriculture".split(",")))


        content = Content.objects.create(
        title="Accuracy Assessment of a Land Cover Classification",
        description="Accuracy Assessment of a Land Cover Classification",
        skill_level= ADVANCE,
        date= "2022-08-02 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-satellite-remote-sensing-measuring-urban-heat-islands-and",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("All".split(",")))


        content = Content.objects.create(
        title="Agricultural Crop Classification with Synthetic Aperture Radar and Optical Remote Sensing",
        description="Agricultural Crop Classification with Synthetic Aperture Radar and Optical Remote Sensing",
        skill_level= BEGINNER,
        date= "2022-08-12 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-monitoring-aquatic-vegetation-remote-sensing",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("All".split(",")))


        content = Content.objects.create(
        title="An Inside Look at How NASA Measures Air Pollution",
        description="An Inside Look at How NASA Measures Air Pollution",
        skill_level= BEGINNER,
        date= "2022-08-12 00:00:00",
        language= "Spanish",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/spanish/arset-monitoreo-de-la-vegetacion-acuatica-con-teledeteccion",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Capacity Building".split(",")))


        content = Content.objects.create(
        title="Applications of GPM IMERG Reanalysis for Assessing Extreme Dry and Wet Periods",
        description="Applications of GPM IMERG Reanalysis for Assessing Extreme Dry and Wet Periods",
        skill_level= BEGINNER,
        date= "2022-08-14 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-humanitarian-applications-using-nasa-earth-observations",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Climate".split(",")))


        content = Content.objects.create(
        title="Applications of Remote Sensing to Soil Moisture and Evapotranspiration",
        description="Applications of Remote Sensing to Soil Moisture and Evapotranspiration",
        skill_level= INTERMEDIATE,
        date= "2022-08-01 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-applications-remote-sensing-based-evapotranspiration-data",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Climate".split(",")))


        content = Content.objects.create(
        title="Applications of Remote Sensing-Based Evapotranspiration Data Products for Agricultural and Water Resource Management",
        description="Applications of Remote Sensing-Based Evapotranspiration Data Products for Agricultural and Water Resource Management",
        skill_level= BEGINNER,
        date= "2022-08-24 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-measuring-atmospheric-carbon-dioxide-space-support-climate",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Climate".split(",")))


        content = Content.objects.create(
        title="Applications of Satellite Observations for Air Quality and Health Exposure",
        description="Applications of Satellite Observations for Air Quality and Health Exposure",
        skill_level= BEGINNER,
        date= "2022-08-24 00:00:00",
        language= "Spanish",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/spanish/arset-medicion-del-dioxido-de-carbono-atmosferico-desde-el-espacio-en",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Climate".split(",")))


        content = Content.objects.create(
        title="Atmospheric CO2 and CH4 Budgets to Support the Global Stocktake",
        description="Atmospheric CO2 and CH4 Budgets to Support the Global Stocktake",
        skill_level= BEGINNER,
        date= "2022-08-11 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-atmospheric-co2-and-ch4-budgets-support-global-stocktake",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Climate".split(",")))


        content = Content.objects.create(
        title="Caja de Herramientas (Toolkit) de Observaciones de la Tierra para Ciudades y Asentamientos Humanos Sostenibles",
        description="Caja de Herramientas (Toolkit) de Observaciones de la Tierra para Ciudades y Asentamientos Humanos Sostenibles",
        skill_level= INTERMEDIATE,
        date= "2022-08-14 00:00:00",
        language= "Spanish",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/spanish/arset-utilizar-el-un-biodiversity-lab-para-tomar-el-pulso-del-planeta",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Climate".split(",")))


        content = Content.objects.create(
        title="Change Detection for Land Cover Mapping",
        description="Change Detection for Land Cover Mapping",
        skill_level= INTERMEDIATE,
        date= "2022-08-14 00:00:00",
        language= "French",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/french/arset-utiliser-le-un-biodiversity-lab-pour-surveiller-le-pouls-de-la",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Climate".split(",")))


        content = Content.objects.create(
        title="Clasificaci�n de Cultivos Agr�colas con Radar de Apertura Sint�tica y Teledetecci�n �ptica",
        description="Clasificaci�n de Cultivos Agr�colas con Radar de Apertura Sint�tica y Teledetecci�n �ptica",
        skill_level= INTERMEDIATE,
        date= "2022-08-14 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-using-un-biodiversity-lab-monitor-pulse-planet",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Climate, Disasters, Eco Forecasting, Health & Air Quality".split(",")))


        content = Content.objects.create(
        title="Creating and Using Normalized Difference Vegetation Index (NDVI) from Satellite Imagery",
        description="Creating and Using Normalized Difference Vegetation Index (NDVI) from Satellite Imagery",
        skill_level= ADVANCE,
        date= "2022-08-12 00:00:00",
        language= "Spanish",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/spanish/arset-mapeo-de-cultivos-y-sus-caracteristicas-biofisicas-con-sar",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Climate, Disasters, Eco Forecasting, Health & Air Quality".split(",")))


        content = Content.objects.create(
        title="Data Analysis Tools for High Resolution Air Quality Satellite Datasets",
        description="Data Analysis Tools for High Resolution Air Quality Satellite Datasets",
        skill_level= ADVANCE,
        date= "2022-08-12 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-mapping-crops-and-their-biophysical-characteristics",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Climate, Water Resources".split(",")))


        content = Content.objects.create(
        title="Earth Observations for Disaster Risk Assessment & Resilience",
        description="Earth Observations for Disaster Risk Assessment & Resilience",
        skill_level= ADVANCE,
        date= "2022-08-22 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-tools-analyzing-nasa-air-quality-model-output",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="Earth Observations for Indigenous-Led Land Management",
        description="Earth Observations for Indigenous-Led Land Management",
        skill_level= BEGINNER,
        date= "2022-08-27 00:00:00",
        language= "Spanish",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/spanish/arset-caja-de-herramientas-toolkit-de-observaciones-de-la-tierra-para",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="Earth Observations for Monitoring the UN Sustainable Development Goals",
        description="Earth Observations for Monitoring the UN Sustainable Development Goals",
        skill_level= BEGINNER,
        date= "2022-08-27 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-earth-observations-toolkit-sustainable-cities-and-human",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="Earth Observations Toolkit for Sustainable Cities and Human Settlements",
        description="Earth Observations Toolkit for Sustainable Cities and Human Settlements",
        skill_level= ADVANCE,
        date= "2022-08-18 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-using-earth-observations-pre-and-post-fire-monitoring",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="El Monitoreo de Aguas Subterr�neas Usando Observaciones de las Misiones �Gravity Recovery and Climate Experiment� (GRACE) de la NASA",
        description="El Monitoreo de Aguas Subterr�neas Usando Observaciones de las Misiones �Gravity Recovery and Climate Experiment� (GRACE) de la NASA",
        skill_level= ADVANCE,
        date= "2022-08-30 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-monitoring-coastal-and-estuarine-water-quality-using-remote",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="El Uso de la Fluorescencia Inducida por el Sol y LIDAR para Evaluar los Cambios y la Vulnerabilidad de la Vegetaci�n",
        description="El Uso de la Fluorescencia Inducida por el Sol y LIDAR para Evaluar los Cambios y la Vulnerabilidad de la Vegetaci�n",
        skill_level= INTERMEDIATE,
        date= "2022-08-05 00:00:00",
        language= "Spanish",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/spanish/arset-clasificacion-de-cultivos-agricolas-con-radar-de-apertura",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="Evaluating Ecosystem Services with Remote Sensing",
        description="Evaluating Ecosystem Services with Remote Sensing",
        skill_level= INTERMEDIATE,
        date= "2022-08-05 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-agricultural-crop-classification-synthetic-aperture-radar-and",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="Forest Mapping and Monitoring with SAR Data",
        description="Forest Mapping and Monitoring with SAR Data",
        skill_level= BEGINNER,
        date= "2022-08-29 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-introduction-nasa-resources-climate-change-applications",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="From Earth Observations to Earth Applications: Satellite Applications for Biodiversity Conservation",
        description="From Earth Observations to Earth Applications: Satellite Applications for Biodiversity Conservation",
        skill_level= ADVANCE,
        date= "2022-08-23 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-introduction-and-access-global-air-quality-forecasting-data-and",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="Fundamentals of Remote Sensing",
        description="Fundamentals of Remote Sensing",
        skill_level= INTERMEDIATE,
        date= "2022-08-14 00:00:00",
        language= "Spanish",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/spanish/arset-monitoreo-de-la-calidad-de-aguas-costeras-y-estuarinas-la",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("All".split(",")))


        content = Content.objects.create(
        title="Fundamentals of Satellite Remote Sensing for Health Monitoring",
        description="Fundamentals of Satellite Remote Sensing for Health Monitoring",
        skill_level= INTERMEDIATE,
        date= "2022-08-14 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-monitoring-coastal-and-estuarine-water-quality-transitioning",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="Groundwater Monitoring using Observations from NASA�s Gravity Recovery and Climate Experiment (GRACE) Missions",
        description="Groundwater Monitoring using Observations from NASA�s Gravity Recovery and Climate Experiment (GRACE) Missions",
        skill_level= INTERMEDIATE,
        date= "2022-08-18 00:00:00",
        language= "Spanish",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/spanish/arset-observaciones-de-satelites-para-el-analisis-de-peligros",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="High Resolution NO2 Monitoring From Space with TROPOMI",
        description="High Resolution NO2 Monitoring From Space with TROPOMI",
        skill_level= INTERMEDIATE,
        date= "2022-08-18 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-satellite-observations-analyzing-natural-hazards-small-island",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="High Temporal Resolution Air Quality Observations from Space",
        description="High Temporal Resolution Air Quality Observations from Space",
        skill_level= INTERMEDIATE,
        date= "2022-08-12 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-species-distribution-modeling-remote-sensing",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="Humanitarian Applications Using NASA Earth Observations",
        description="Humanitarian Applications Using NASA Earth Observations",
        skill_level= INTERMEDIATE,
        date= "2022-08-16 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-using-google-earth-engine-land-monitoring-applications",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="Hyperspectral Data for Land and Coastal Systems",
        description="Hyperspectral Data for Land and Coastal Systems",
        skill_level= BEGINNER,
        date= "2022-08-01 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-nasa-earth-observations-energy-management",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="Integrating Remote Sensing into a Water Quality Monitoring Program",
        description="Integrating Remote Sensing into a Water Quality Monitoring Program",
        skill_level= INTERMEDIATE,
        date= "2022-08-11 00:00:00",
        language= "Spanish",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/spanish/arset-observaciones-de-satelites-y-herramientas-para-el-riesgo",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="Introducci�n a los Datos de Luces Nocturnas de NASA \"Black Marble\"",
        description="Introducci�n a los Datos de Luces Nocturnas de NASA \"Black Marble\"",
        skill_level= INTERMEDIATE,
        date= "2022-08-11 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-satellite-observations-and-tools-fire-risk-detection-and",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="Introducci�n al Radar de Apertura Sint�tica",
        description="Introducci�n al Radar de Apertura Sint�tica",
        skill_level= BEGINNER,
        date= "2022-08-30 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-introduction-population-grids-and-their-integration-remote",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="Introduction and Access to Global Air Quality Forecasting Data and Tools",
        description="Introduction and Access to Global Air Quality Forecasting Data and Tools",
        skill_level= BEGINNER,
        date= "2022-08-16 00:00:00",
        language= "Spanish",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/spanish/arset-el-uso-de-la-fluorescencia-inducida-por-el-sol-y-lidar-para",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="Introduction to Global Precipitation Measurement (GPM) Data and Applications",
        description="Introduction to Global Precipitation Measurement (GPM) Data and Applications",
        skill_level= BEGINNER,
        date= "2022-08-16 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-use-solar-induced-fluorescence-and-lidar-assess-vegetation",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="Introduction to NASA Resources for Climate Change Applications",
        description="Introduction to NASA Resources for Climate Change Applications",
        skill_level= BEGINNER,
        date= "2022-08-09 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-mapping-and-monitoring-lakes-and-reservoirs-satellite",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="Introduction to NASA�s \"Black Marble\" Night Lights Data",
        description="Introduction to NASA�s \"Black Marble\" Night Lights Data",
        skill_level= BEGINNER,
        date= "2022-08-19 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-hyperspectral-data-land-and-coastal-systems",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="Introduction to Population Grids and their Integration with Remote Sensing Data for Sustainable Development and Disaster Management",
        description="Introduction to Population Grids and their Integration with Remote Sensing Data for Sustainable Development and Disaster Management",
        skill_level= BEGINNER,
        date= "2022-08-03 00:00:00",
        language= "Spanish",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/spanish/arset-introduccion-los-datos-de-luces-nocturnas-de-nasa-black-marble",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="Introduction to Remote Sensing for Coastal and Ocean Applications",
        description="Introduction to Remote Sensing for Coastal and Ocean Applications",
        skill_level= BEGINNER,
        date= "2022-08-03 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-introduction-nasas-black-marble-night-lights-data",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="Introduction to Remote Sensing for Conservation Management",
        description="Introduction to Remote Sensing for Conservation Management",
        skill_level= BEGINNER,
        date= "2022-08-10 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-satellite-remote-sensing-urban-heat-islands",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="Introduction to Remote Sensing for Scenario-Based Ecoforecasting",
        description="Introduction to Remote Sensing for Scenario-Based Ecoforecasting",
        skill_level= BEGINNER,
        date= "2022-08-05 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-remote-sensing-mangroves-support-un-sustainable-development",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="Introduction to Remote Sensing for Wildfire Applications",
        description="Introduction to Remote Sensing for Wildfire Applications",
        skill_level= ADVANCE,
        date= "2022-08-22 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-modis-viirs-transition-air-quality-applications",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="Introduction to Remote Sensing for Wildfire Applications",
        description="Introduction to Remote Sensing for Wildfire Applications",
        skill_level= BEGINNER,
        date= "2022-08-25 00:00:00",
        language= "Spanish",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/spanish/arset-teledeteccion-de-ecosistemas-costeros",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="Introduction to Remote Sensing of Harmful Algal Blooms",
        description="Introduction to Remote Sensing of Harmful Algal Blooms",
        skill_level= BEGINNER,
        date= "2022-08-25 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-remote-sensing-coastal-ecosystems",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="Introduction to Satellite Remote Sensing for Air Quality Applications",
        description="Introduction to Satellite Remote Sensing for Air Quality Applications",
        skill_level= ADVANCE,
        date= "2022-08-21 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-using-earth-observations-monitor-water-budgets-river-basin",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="Introduction to Synthetic Aperture Radar",
        description="Introduction to Synthetic Aperture Radar",
        skill_level= BEGINNER,
        date= "2022-08-30 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-understanding-phenology-remote-sensing",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters".split(",")))


        content = Content.objects.create(
        title="Introduction to Using the VIC Hydrologic Model with NASA Earth Observations",
        description="Introduction to Using the VIC Hydrologic Model with NASA Earth Observations",
        skill_level= BEGINNER,
        date= "2022-08-25 00:00:00",
        language= "Spanish",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/spanish/arset-el-monitoreo-de-aguas-subterraneas-usando-observaciones-de-las",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters, Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Investigating Time Series of Satellite Imagery",
        description="Investigating Time Series of Satellite Imagery",
        skill_level= BEGINNER,
        date= "2022-08-25 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-groundwater-monitoring-using-observations-nasas-gravity",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters, Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="La Teledetecci�n por Radar y sus Aplicaciones para la Tierra, el Agua y Desastres",
        description="La Teledetecci�n por Radar y sus Aplicaciones para la Tierra, el Agua y Desastres",
        skill_level= BEGINNER,
        date= "2022-08-26 00:00:00",
        language= "Spanish",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/spanish/arset-un-vistazo-como-la-nasa-mide-la-contaminacion-del-aire",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Disasters, Health & Air Quality".split(",")))


        content = Content.objects.create(
        title="Land Cover Classification with Satellite Imagery",
        description="Land Cover Classification with Satellite Imagery",
        skill_level= BEGINNER,
        date= "2022-08-26 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-inside-look-how-nasa-measures-air-pollution",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Mapeo de Cultivos y sus Caracter�sticas Biof�sicas con SAR Polarim�trico y Teledetecci�n �ptica",
        description="Mapeo de Cultivos y sus Caracter�sticas Biof�sicas con SAR Polarim�trico y Teledetecci�n �ptica",
        skill_level= ADVANCE,
        date= "2022-08-12 00:00:00",
        language= "Spanish",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/spanish/arset-mapeo-y-monitoreo-de-los-bosques-con-datos-sar",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Mapeo y Monitoreo de los Bosques con Datos SAR",
        description="Mapeo y Monitoreo de los Bosques con Datos SAR",
        skill_level= ADVANCE,
        date= "2022-08-12 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-forest-mapping-and-monitoring-sar-data",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Mapping and Monitoring Lakes and Reservoirs with Satellite Observations",
        description="Mapping and Monitoring Lakes and Reservoirs with Satellite Observations",
        skill_level= BEGINNER,
        date= "2022-08-14 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-satellite-remote-sensing-agricultural-applications",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Mapping Crops and their Biophysical Characteristics with Polarimetric SAR and Optical Remote Sensing",
        description="Mapping Crops and their Biophysical Characteristics with Polarimetric SAR and Optical Remote Sensing",
        skill_level= BEGINNER,
        date= "2022-08-24 00:00:00",
        language= "French",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/french/arset-utiliser-le-un-biodiversity-lab-pour-soutenir-les-objectifs",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Measuring Atmospheric Carbon Dioxide from Space in Support of Climate Related Studies",
        description="Measuring Atmospheric Carbon Dioxide from Space in Support of Climate Related Studies",
        skill_level= BEGINNER,
        date= "2022-08-24 00:00:00",
        language= "Spanish",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/spanish/arset-utilizando-el-un-biodiversity-lab-para-apoyar-los-objetivos",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Medici�n del Di�xido de Carbono Atmosf�rico desde el Espacio en Apoyo a los Estudios Relacionados Con el Clima",
        description="Medici�n del Di�xido de Carbono Atmosf�rico desde el Espacio en Apoyo a los Estudios Relacionados Con el Clima",
        skill_level= BEGINNER,
        date= "2022-08-24 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-using-un-biodiversity-lab-support-national-conservation-and",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Methods in Using NASA Remote Sensing for Health Applications",
        description="Methods in Using NASA Remote Sensing for Health Applications",
        skill_level= ADVANCE,
        date= "2022-08-28 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-applications-gpm-imerg-reanalysis-assessing-extreme-dry-and-wet",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="MODIS to VIIRS Transition for Air Quality Applications",
        description="MODIS to VIIRS Transition for Air Quality Applications",
        skill_level= ADVANCE,
        date= "2022-08-03 00:00:00",
        language= "Spanish",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/spanish/arset-sar-para-desastres-y-aplicaciones-hidrologicas",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Monitoreo de la Calidad de Aguas Costeras y Estuarinas: La Transici�n de MODIS a VIIRS",
        description="Monitoreo de la Calidad de Aguas Costeras y Estuarinas: La Transici�n de MODIS a VIIRS",
        skill_level= ADVANCE,
        date= "2022-08-03 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-sar-disasters-and-hydrological-applications",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Monitoreo de la Vegetaci�n Acu�tica con Teledetecci�n",
        description="Monitoreo de la Vegetaci�n Acu�tica con Teledetecci�n",
        skill_level= BEGINNER,
        date= "2022-08-26 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-river-basin-delineation-based-nasa-digital-elevation-data",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Monitoring Aquatic Vegetation with Remote Sensing",
        description="Monitoring Aquatic Vegetation with Remote Sensing",
        skill_level= BEGINNER,
        date= "2022-08-20 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-new-sensor-highlight-ecostress",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Monitoring Coastal and Estuarine Water Quality Using Remote Sensing and In Situ Data",
        description="Monitoring Coastal and Estuarine Water Quality Using Remote Sensing and In Situ Data",
        skill_level= BEGINNER,
        date= "2022-08-09 00:00:00",
        language= "English",
        type="in_person",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-applications-satellite-observations-air-quality-and-health",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Monitoring Coastal and Estuarine Water Quality: Transitioning from MODIS to VIIRS",
        description="Monitoring Coastal and Estuarine Water Quality: Transitioning from MODIS to VIIRS",
        skill_level= INTERMEDIATE,
        date= "2022-08-17 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-remote-sensing-freshwater-habitats",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Monitoring Tropical Storms for Emergency Preparedness",
        description="Monitoring Tropical Storms for Emergency Preparedness",
        skill_level= ADVANCE,
        date= "2022-08-28 00:00:00",
        language= "Spanish",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/spanish/arset-sar-y-sus-aplicaciones-para-la-cobertura-terrestre",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Monitoring Urban Floods Using Remote Sensing",
        description="Monitoring Urban Floods Using Remote Sensing",
        skill_level= ADVANCE,
        date= "2022-08-28 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-sar-landcover-applications",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="NASA Earth Observations for Energy Management",
        description="NASA Earth Observations for Energy Management",
        skill_level= BEGINNER,
        date= "2022-08-06 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-earth-observations-disaster-risk-assessment-resilience",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="NASA Earth Science Data for Wildland Fire Decision Making",
        description="NASA Earth Science Data for Wildland Fire Decision Making",
        skill_level= ADVANCE,
        date= "2022-08-09 00:00:00",
        language= "Spanish",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/spanish/arset-teledeteccion-para-el-monitoreo-de-los-ods-sobre-la-degradacion",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="NASA Remote Sensing for Flood Monitoring and Management",
        description="NASA Remote Sensing for Flood Monitoring and Management",
        skill_level= ADVANCE,
        date= "2022-08-09 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/advanced-webinar-remote-sensing-monitoring-land-degradation-and-sustainable",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="NASA Remote Sensing Observations for Flood Management",
        description="NASA Remote Sensing Observations for Flood Management",
        skill_level= BEGINNER,
        date= "2022-08-17 00:00:00",
        language= "Spanish",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/spanish/arset-una-sesion-de-preguntas-y-respuestas-sobre-la-teledeteccion-por",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="New Sensor Highlight: ECOSTRESS",
        description="New Sensor Highlight: ECOSTRESS",
        skill_level= BEGINNER,
        date= "2022-08-17 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/qa-session-radar-remote-sensing",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Observaciones de la Tierra para su Gesti�n a Cargo de Pueblos Ind�genas",
        description="Observaciones de la Tierra para su Gesti�n a Cargo de Pueblos Ind�genas",
        skill_level= ADVANCE,
        date= "2022-08-05 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-integrating-remote-sensing-water-quality-monitoring-program",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Observaciones de Sat�lites para el An�lisis de Peligros Naturales en los Peque�os Estados Insulares",
        description="Observaciones de Sat�lites para el An�lisis de Peligros Naturales en los Peque�os Estados Insulares",
        skill_level= ADVANCE,
        date= "2022-08-28 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-high-resolution-no2-monitoring-space-tropomi",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Observaciones de Sat�lites y Herramientas para el Riesgo, Detecci�n y An�lisis de Incendios",
        description="Observaciones de Sat�lites y Herramientas para el Riesgo, Detecci�n y An�lisis de Incendios",
        skill_level= INTERMEDIATE,
        date= "2022-08-16 00:00:00",
        language= "Spanish",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/spanish/arset-teledeteccion-para-escenarios-de-desastres",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Overview of the Global Disaster Alert and Coordination System (GDACS)",
        description="Overview of the Global Disaster Alert and Coordination System (GDACS)",
        skill_level= INTERMEDIATE,
        date= "2022-08-16 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-remote-sensing-disasters-scenarios",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Procesamiento de Im�genes Satelitales para el Monitoreo de la Calidad del Agua",
        description="Procesamiento de Im�genes Satelitales para el Monitoreo de la Calidad del Agua",
        skill_level= ADVANCE,
        date= "2022-08-15 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/advanced-webinar-investigating-time-series-satellite-imagery",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Processing Satellite Imagery for Monitoring Water Quality",
        description="Processing Satellite Imagery for Monitoring Water Quality",
        skill_level= BEGINNER,
        date= "2022-08-13 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-using-earth-observations-monitor-water-budgets-river-basin-0",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Radar Remote Sensing for Land, Water, & Disaster Applications",
        description="Radar Remote Sensing for Land, Water, & Disaster Applications",
        skill_level= BEGINNER,
        date= "2022-08-05 00:00:00",
        language= "Spanish",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/spanish/arset-observaciones-de-la-tierra-para-su-gestion-cargo-de-pueblos",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Remote Sensing for Conservation & Biodiversity",
        description="Remote Sensing for Conservation & Biodiversity",
        skill_level= BEGINNER,
        date= "2022-08-05 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-earth-observations-indigenous-led-land-management",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Remote Sensing for Disasters Scenarios",
        description="Remote Sensing for Disasters Scenarios",
        skill_level= BEGINNER,
        date= "2022-08-22 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-remote-sensing-conservation-biodiversity",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Remote Sensing for Freshwater Habitats",
        description="Remote Sensing for Freshwater Habitats",
        skill_level= ADVANCE,
        date= "2022-08-18 00:00:00",
        language= "English",
        type="in_person",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-satellite-remote-sensing-air-quality",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Remote Sensing for Mangroves in Support of the UN Sustainable Development Goals",
        description="Remote Sensing for Mangroves in Support of the UN Sustainable Development Goals",
        skill_level= ADVANCE,
        date= "2022-08-18 00:00:00",
        language= "English",
        type="in_person",
        link= "https://appliedsciences.nasa.gov/join-mission/training/satellite-remote-sensing-flood-monitoring-and-management",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Remote Sensing for Monitoring Land Degradation and Sustainable Cities SDGs",
        description="Remote Sensing for Monitoring Land Degradation and Sustainable Cities SDGs",
        skill_level= ADVANCE,
        date= "2022-08-28 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-change-detection-land-cover-mapping",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Remote Sensing of Coastal Ecosystems",
        description="Remote Sensing of Coastal Ecosystems",
        skill_level= BEGINNER,
        date= "2022-08-04 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-high-temporal-resolution-air-quality-observations-space",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Remote Sensing of Drought",
        description="Remote Sensing of Drought",
        skill_level= ADVANCE,
        date= "2022-08-05 00:00:00",
        language= "Spanish",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/spanish/arset-procesamiento-de-imagenes-satelitales-para-el-monitoreo-de-la",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting".split(",")))


        content = Content.objects.create(
        title="Remote Sensing of Forest Cover and Change Assessment for Carbon Monitoring",
        description="Remote Sensing of Forest Cover and Change Assessment for Carbon Monitoring",
        skill_level= ADVANCE,
        date= "2022-08-05 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-processing-satellite-imagery-monitoring-water-quality",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting, Agriculture".split(",")))


        content = Content.objects.create(
        title="Remote Sensing of Land Indicators for Sustainable Development Goal 15",
        description="Remote Sensing of Land Indicators for Sustainable Development Goal 15",
        skill_level= ADVANCE,
        date= "2022-08-07 00:00:00",
        language= "Spanish",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/spanish/arset-la-teledeteccion-por-radar-y-sus-aplicaciones-para-la-tierra-el",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting, Water Resources".split(",")))


        content = Content.objects.create(
        title="Remote Sensing Training: Methods & Best Practices",
        description="Remote Sensing Training: Methods & Best Practices",
        skill_level= ADVANCE,
        date= "2022-08-07 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-radar-remote-sensing-land-water-disaster-applications",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting, Water Resources".split(",")))


        content = Content.objects.create(
        title="River Basin Delineation Based on NASA Digital Elevation Data",
        description="River Basin Delineation Based on NASA Digital Elevation Data",
        skill_level= BEGINNER,
        date= "2022-08-25 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-monitoring-urban-floods-using-remote-sensing",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Eco Forecasting, Water Resources".split(",")))


        content = Content.objects.create(
        title="SAR for Disasters and Hydrological Applications",
        description="SAR for Disasters and Hydrological Applications",
        skill_level= BEGINNER,
        date= "2022-08-30 00:00:00",
        language= "English",
        type="in_person",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-earth-observations-monitoring-un-sustainable-development-goals",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Health & Air Quality".split(",")))


        content = Content.objects.create(
        title="SAR for Landcover Applications",
        description="SAR for Landcover Applications",
        skill_level= ADVANCE,
        date= "2022-08-10 00:00:00",
        language= "English",
        type="in_person",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-satellite-remote-sensing-dust-fires-smoke-and-air-quality",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Health & Air Quality".split(",")))


        content = Content.objects.create(
        title="SAR para Desastres y Aplicaciones Hidrol�gicas",
        description="SAR para Desastres y Aplicaciones Hidrol�gicas",
        skill_level= ADVANCE,
        date= "2022-08-11 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-techniques-wildfire-detection-and-monitoring",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Health & Air Quality".split(",")))


        content = Content.objects.create(
        title="SAR y sus Aplicaciones para la Cobertura Terrestre",
        description="SAR y sus Aplicaciones para la Cobertura Terrestre",
        skill_level= BEGINNER,
        date= "2022-08-03 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-monitoring-tropical-storms-emergency-preparedness",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Health & Air Quality".split(",")))


        content = Content.objects.create(
        title="Satellite Derived Annual PM2.5 Datasets in Support of United Nations Sustainable Development Goals",
        description="Satellite Derived Annual PM2.5 Datasets in Support of United Nations Sustainable Development Goals",
        skill_level= BEGINNER,
        date= "2022-08-15 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-introduction-using-vic-hydrologic-model-nasa-earth-observations",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Health & Air Quality".split(",")))


        content = Content.objects.create(
        title="Satellite Observations and Tools for Fire Risk, Detection, and Analysis",
        description="Satellite Observations and Tools for Fire Risk, Detection, and Analysis",
        skill_level= ADVANCE,
        date= "2022-08-13 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-accuracy-assessment-land-cover-classification",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Health & Air Quality".split(",")))


        content = Content.objects.create(
        title="Satellite Observations for Analyzing Natural Hazards on Small Island Nations",
        description="Satellite Observations for Analyzing Natural Hazards on Small Island Nations",
        skill_level= ADVANCE,
        date= "2022-08-17 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-data-analysis-tools-high-resolution-air-quality-satellite",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Health & Air Quality".split(",")))


        content = Content.objects.create(
        title="Satellite Remote Sensing for Agricultural Applications",
        description="Satellite Remote Sensing for Agricultural Applications",
        skill_level= BEGINNER,
        date= "2022-08-07 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-introduction-remote-sensing-scenario-based-ecoforecasting",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Health & Air Quality".split(",")))


        content = Content.objects.create(
        title="Satellite Remote Sensing for Measuring Urban Heat Islands and Constructing Heat Vulnerability Indices",
        description="Satellite Remote Sensing for Measuring Urban Heat Islands and Constructing Heat Vulnerability Indices",
        skill_level= BEGINNER,
        date= "2022-08-05 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-introduction-remote-sensing-harmful-algal-blooms",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Health & Air Quality".split(",")))


        content = Content.objects.create(
        title="Satellite Remote Sensing for Urban Heat Islands",
        description="Satellite Remote Sensing for Urban Heat Islands",
        skill_level= ADVANCE,
        date= "2022-08-12 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-remote-sensing-drought",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Health & Air Quality".split(",")))


        content = Content.objects.create(
        title="Satellite Remote Sensing of Air Quality",
        description="Satellite Remote Sensing of Air Quality",
        skill_level= BEGINNER,
        date= "2022-08-28 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-introduction-synthetic-aperture-radar",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Health & Air Quality".split(",")))


        content = Content.objects.create(
        title="Satellite Remote Sensing of Dust, Fires, Smoke, and Air Quality",
        description="Satellite Remote Sensing of Dust, Fires, Smoke, and Air Quality",
        skill_level= BEGINNER,
        date= "2022-08-28 00:00:00",
        language= "Spanish",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/spanish/arset-introduccion-al-radar-de-apertura-sintetica",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Health & Air Quality".split(",")))


        content = Content.objects.create(
        title="Satellite Remote Sensing of Flood Monitoring and Management",
        description="Satellite Remote Sensing of Flood Monitoring and Management",
        skill_level= INTERMEDIATE,
        date= "2022-08-20 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-remote-sensing-land-indicators-sustainable-development-goal-15",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Health & Air Quality".split(",")))


        content = Content.objects.create(
        title="Satellite Remote Sensing of Particulate Matter Air Quality",
        description="Satellite Remote Sensing of Particulate Matter Air Quality",
        skill_level= ADVANCE,
        date= "2022-08-01 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-methods-using-nasa-remote-sensing-health-applications",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Health & Air Quality".split(",")))


        content = Content.objects.create(
        title="Species Distribution Modeling with Remote Sensing",
        description="Species Distribution Modeling with Remote Sensing",
        skill_level= ADVANCE,
        date= "2022-08-18 00:00:00",
        language= "English",
        type="in_person",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-nasa-remote-sensing-flood-monitoring-and-management",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Health & Air Quality".split(",")))


        content = Content.objects.create(
        title="Techniques for Wildfire Detection and Monitoring",
        description="Techniques for Wildfire Detection and Monitoring",
        skill_level= INTERMEDIATE,
        date= "2022-08-03 00:00:00",
        language= "English",
        type="in_person",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-nasa-earth-science-data-wildland-fire-decision-making",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Water Resources".split(",")))


        content = Content.objects.create(
        title="Teledetecci�n de Ecosistemas Costeros",
        description="Teledetecci�n de Ecosistemas Costeros",
        skill_level= INTERMEDIATE,
        date= "2022-08-15 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-satellite-derived-annual-pm25-datasets-support-united-nations",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Water Resources".split(",")))


        content = Content.objects.create(
        title="Teledetecci�n para el Monitoreo de los ODS sobre la Degradaci�n de Tierras y Ciudades Sostenibles",
        description="Teledetecci�n para el Monitoreo de los ODS sobre la Degradaci�n de Tierras y Ciudades Sostenibles",
        skill_level= BEGINNER,
        date= "2022-08-21 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-overview-global-disaster-alert-and-coordination-system-gdacs",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Water Resources".split(",")))


        content = Content.objects.create(
        title="Teledetecci�n para Escenarios de Desastres",
        description="Teledetecci�n para Escenarios de Desastres",
        skill_level= ADVANCE,
        date= "2022-08-31 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-land-cover-classification-satellite-imagery",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Water Resources".split(",")))


        content = Content.objects.create(
        title="Tools for Analyzing NASA Air Quality Model Output",
        description="Tools for Analyzing NASA Air Quality Model Output",
        skill_level= INTERMEDIATE,
        date= "2022-08-13 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-remote-sensing-training-methods-best-practices",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Water Resources".split(",")))


        content = Content.objects.create(
        title="Un Vistazo a C�mo la NASA Mide la Contaminaci�n del Aire",
        description="Un Vistazo a C�mo la NASA Mide la Contaminaci�n del Aire",
        skill_level= INTERMEDIATE,
        date= "2022-08-01 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-applications-remote-sensing-soil-moisture-and",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Water Resources".split(",")))


        content = Content.objects.create(
        title="Una Sesi�n de Preguntas y Respuestas sobre la Teledetecci�n por Radar",
        description="Una Sesi�n de Preguntas y Respuestas sobre la Teledetecci�n por Radar",
        skill_level= BEGINNER,
        date= "2022-08-04 00:00:00",
        language= "English",
        type="in_person",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-earth-observations-earth-applications-satellite-applications",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Water Resources".split(",")))


        content = Content.objects.create(
        title="Understanding Phenology with Remote Sensing",
        description="Understanding Phenology with Remote Sensing",
        skill_level= BEGINNER,
        date= "2022-08-06 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-introduction-satellite-remote-sensing-air-quality-applications",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Water Resources".split(",")))


        content = Content.objects.create(
        title="Use of Solar Induced Fluorescence and LIDAR to Assess Vegetation Change and Vulnerability",
        description="Use of Solar Induced Fluorescence and LIDAR to Assess Vegetation Change and Vulnerability",
        skill_level= INTERMEDIATE,
        date= "2022-08-06 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-introduction-remote-sensing-coastal-and-ocean-applications",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Water Resources".split(",")))


        content = Content.objects.create(
        title="Using Earth Observations for Pre- and Post-Fire Monitoring",
        description="Using Earth Observations for Pre- and Post-Fire Monitoring",
        skill_level= INTERMEDIATE,
        date= "2022-08-09 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-remote-sensing-forest-cover-and-change-assessment-carbon",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Water Resources".split(",")))


        content = Content.objects.create(
        title="Using Earth Observations to Monitor Water Budgets for River Basin Management",
        description="Using Earth Observations to Monitor Water Budgets for River Basin Management",
        skill_level= INTERMEDIATE,
        date= "2022-08-09 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-using-nasa-remote-sensing-disaster-management",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Water Resources".split(",")))


        content = Content.objects.create(
        title="Using Earth Observations to Monitor Water Budgets for River Basin Management II",
        description="Using Earth Observations to Monitor Water Budgets for River Basin Management II",
        skill_level= BEGINNER,
        date= "2022-08-02 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-fundamentals-satellite-remote-sensing-health-monitoring",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Water Resources".split(",")))


        content = Content.objects.create(
        title="Using Google Earth Engine for Land Monitoring Applications",
        description="Using Google Earth Engine for Land Monitoring Applications",
        skill_level= ADVANCE,
        date= "2022-08-16 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-using-nasa-remote-sensing-flood-monitoring-and-management",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Water Resources".split(",")))


        content = Content.objects.create(
        title="Using NASA Remote Sensing for Disaster Management",
        description="Using NASA Remote Sensing for Disaster Management",
        skill_level= ADVANCE,
        date= "2022-08-10 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-creating-and-using-normalized-difference-vegetation-index-ndvi",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Water Resources".split(",")))


        content = Content.objects.create(
        title="Using NASA Remote Sensing for Flood Monitoring and Management",
        description="Using NASA Remote Sensing for Flood Monitoring and Management",
        skill_level= BEGINNER,
        date= "2022-08-13 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-water-resource-management-using-nasa-earth-science-data",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Water Resources".split(",")))


        content = Content.objects.create(
        title="Using the UN Biodiversity Lab to Monitor the Pulse of the Planet",
        description="Using the UN Biodiversity Lab to Monitor the Pulse of the Planet",
        skill_level= ADVANCE,
        date= "2022-08-01 00:00:00",
        language= "English",
        type="in_person",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-satellite-remote-sensing-particulate-matter-air-quality",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Water Resources".split(",")))


        content = Content.objects.create(
        title="Using the UN Biodiversity Lab to Support National Conservation and Sustainable Development Goals",
        description="Using the UN Biodiversity Lab to Support National Conservation and Sustainable Development Goals",
        skill_level= INTERMEDIATE,
        date= "2022-08-06 00:00:00",
        language= "English",
        type="in_person",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-introduction-remote-sensing-wildfire-applications",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Water Resources".split(",")))


        content = Content.objects.create(
        title="Utiliser le UN Biodiversity Lab pour soutenir les objectifs nationaux de conservation et de d�veloppement durable",
        description="Utiliser le UN Biodiversity Lab pour soutenir les objectifs nationaux de conservation et de d�veloppement durable",
        skill_level= BEGINNER,
        date= "2022-08-08 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-nasa-remote-sensing-observations-flood-management",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Water Resources".split(",")))


        content = Content.objects.create(
        title="Utiliser le UN Biodiversity Lab pour Surveiller le Pouls de la Plan�te",
        description="Utiliser le UN Biodiversity Lab pour Surveiller le Pouls de la Plan�te",
        skill_level= BEGINNER,
        date= "2022-08-05 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-introduction-remote-sensing-conservation-management",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Water Resources".split(",")))


        content = Content.objects.create(
        title="Utilizando el UN Biodiversity Lab para Apoyar los Objetivos Nacionales de Conservaci�n y Desarrollo Sostenible",
        description="Utilizando el UN Biodiversity Lab para Apoyar los Objetivos Nacionales de Conservaci�n y Desarrollo Sostenible",
        skill_level= BEGINNER,
        date= "2022-08-31 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-introduction-remote-sensing-wildfire-applications-0",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Water Resources".split(",")))


        content = Content.objects.create(
        title="Utilizar el UN Biodiversity Lab para Tomar el Pulso del Planeta",
        description="Utilizar el UN Biodiversity Lab para Tomar el Pulso del Planeta",
        skill_level= BEGINNER,
        date= "2022-08-17 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-introduction-global-precipitation-measurement-gpm-data-and",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Water Resources".split(",")))


        content = Content.objects.create(
        title="Water Resource Management Using NASA Earth Science Data",
        description="Water Resource Management Using NASA Earth Science Data",
        skill_level= BEGINNER,
        date= "2022-08-23 00:00:00",
        language= "English",
        type="online",
        link= "https://appliedsciences.nasa.gov/join-mission/training/english/arset-fundamentals-remote-sensing",
        creator=CONTENT_CREATOR
        )
        content.thematic_area.add(*tuple("Water Resources".split(",")))
