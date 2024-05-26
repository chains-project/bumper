```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final java.util.Set<org.pitest.classinfo.ClassName> classInfo = java.util.Collections.singleton(data.getMutatedClass());
    final org.pitest.coverage.CoverageData coverageData = coverage.getCoverageData(classInfo);
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverageData.getClassInfo(classInfo));
}
```