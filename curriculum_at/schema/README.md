Problem: CurriculumStructure is only contained by the Lesson
LearningStandardDocument: references (not contains) to top most LearningStandardItem: then each Item links to its predecessor and document
Lesson: links to one or more LearningStandardItems 
```
<ContentCatalog RefId="359D75101AD0A9D7A8C3DAD0A85103A2" xml:lang="en">
  <ContentObject>
    <Location ReferenceType="URI">http://myserver.mydomain.com/content/civil_war_photos.pdf</Location>
  </ContentObject>
  <Status>Available</Status>
  <Title>The Civil War in Photos</Title>
  <Description>A collection of Civil War Photos</Description>
  <Author>John Smith</Author>
  <LanguageCode>eng</LanguageCode>
  <GradeLevels>
    <GradeLevel>
      <Code>09</Code>
    </GradeLevel>
    <GradeLevel>
      <Code>10</Code>
    </GradeLevel>
    <GradeLevel>
      <Code>11</Code>
    </GradeLevel>
  </GradeLevels>
  <SubjectAreas>
    <SubjectArea>
      <Code>04</Code>
    </SubjectArea>
  </SubjectAreas>
  <MediaTypes>
    <MediaType>x-application/pdf</MediaType>
  </MediaTypes>
  <LearningStandards>
    <Document>
      <Title>Essential Academic Learning Requirements</Title>
      <StandardsSettingBody>
        <Country>US</Country>
        <StateProvince>OH</StateProvince>
        <NCESId>12345</NCESId>
        <SettingBodyName>Ohio Department of Education</SettingBodyName>
      </StandardsSettingBody>
      <StatementCodes>
        <StatementCode>US History.2.03.a</StatementCode>
      </StatementCodes>
    </Document>
    <Document>
      <Title>State Learning Requirements</Title>
      <StandardsSettingBody>
        <Country>US</Country>
        <StateProvince>UT</StateProvince>
        <NCESId>67890</NCESId>
        <SettingBodyName>UT Department of Education</SettingBodyName>
      </StandardsSettingBody>
      <StatementCodes>
        <StatementCode>US History.4.89</StatementCode>
      </StatementCodes>
    </Document>
  </LearningStandards>
  <InstructionalLevel>0571</InstructionalLevel>
  <TechnicalRequirements>
    <TechnicalRequirement>Computer</TechnicalRequirement>
  </TechnicalRequirements>
  <Duration Units="minute">10</Duration>
  <Size>100mb</Size>
</ContentCatalog>



<CurriculumStructure RefId="B364631190F169CD8E3DF2BA2537EC8B" xml:lang="en">
  <Titles>
    <Title>Cellular Concepts</Title>
  </Titles>
  <Description>Reviews basic concepts in Cellular Biology</Description>
  <SubjectArea>
    <Code>03</Code>
    <OtherCodeList>
      <OtherCode Codeset="Text">Life and Physical Sciences</OtherCode>
    </OtherCodeList>
  </SubjectArea>
  <CurriculumHierarchyLevel>
    <Number>4</Number>
    <Name>Unit</Name>
    <Description>http://www.compasslearning.com/hierarchy004</Description>
  </CurriculumHierarchyLevel>
  <PredecessorObjects>
    <CurriculumStructureRefId>3DD3294A068EC899EE586A6FEFFCF0EB</CurriculumStructureRefId>
  </PredecessorObjects>
  <LearningObjectives>
    <LearningObjective>Teach students about the basics of cellular structure and lifecycle.</LearningObjective>
  </LearningObjectives>
  <ComponentObjects>
    <ComponentObject SIF_RefObject="Lesson">3DD3294A068EC899EE586A6FEFFCF0EB</ComponentObject>
    <ComponentObject SIF_RefObject="Lesson">8838B02258673F0094E5B426E59C26BC</ComponentObject>
    <ComponentObject SIF_RefObject="Lesson">D41D8CD98F00B204E9800998ECF8427E</ComponentObject>
    <ComponentObject SIF_RefObject="Lesson">DC3076B304B838BF11AF723DD7D4AED7</ComponentObject>
  </ComponentObjects>
  <LearningStandards>
    <LearningStandardItemRefId>141216334645D859E2CA255B1C3BBD91</LearningStandardItemRefId>
  </LearningStandards>
</CurriculumStructure>
```

