import FWCore.ParameterSet.Config as cms

XMLIdealGeometryESSource = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring(
        'Geometry/CMSCommonData/data/materials/2021/v1/materials.xml',
        'Geometry/CMSCommonData/data/rotations.xml',
        'Geometry/CMSCommonData/data/extend/v2/cmsextent.xml',
        'Geometry/CMSCommonData/data/cavernData/2021/v1/cavernData.xml',
        'Geometry/CMSCommonData/data/cms/2030/v5/cms.xml',
        'Geometry/CMSCommonData/data/eta3/etaMax.xml',
        'Geometry/CMSCommonData/data/cmsMother.xml',
        'Geometry/CMSCommonData/data/caloBase/2030/v6/caloBase.xml',
        'Geometry/CMSCommonData/data/cmsCalo.xml',
        'Geometry/HGCalCommonData/data/hgcalMaterial/v2/hgcalMaterial.xml',
        'Geometry/HGCalCommonData/data/hgcal/v17/hgcal.xml',
        'Geometry/HGCalCommonData/data/hgcalcell/v17/hgcalcell.xml',
        'Geometry/HGCalCommonData/data/hgcalwafer/v17/hgcalwafer.xml',
        'Geometry/HGCalCommonData/data/hgcalEE/v17/hgcalEE.xml',
        'Geometry/CMSCommonData/data/FieldParameters.xml',
    ),
    rootNodeName = cms.string('cms:OCMS')
)
