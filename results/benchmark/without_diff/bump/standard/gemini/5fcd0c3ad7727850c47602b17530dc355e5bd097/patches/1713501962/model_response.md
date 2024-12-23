```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final org.pitest.coverage.CoverageSummary coverageSummary = coverage.calculateBlockCoverageSummary();
    final org.pitest.classinfo.ClassName className = org.pitest.classinfo.ClassName.fromString(data.getMutatedClass());
    final org.pitest.coverage.CoverageData coverageData = coverage.getCoverageData(className);
    if (coverageData == null) {
        return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), null);
    }
    final org.pitest.coverage.BlockCoverage blockCoverage = coverageData.getBlockCoverage();
    final org.pitest.coverage.LineCoverage lineCoverage = coverageData.getLineCoverage();
    final org.pitest.coverage.MethodCoverage methodCoverage = coverageData.getMethodCoverage();
    final org.pitest.coverage.ClassInfo classInfo = new org.pitest.coverage.ClassInfo(className, blockCoverage, lineCoverage, methodCoverage);
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```