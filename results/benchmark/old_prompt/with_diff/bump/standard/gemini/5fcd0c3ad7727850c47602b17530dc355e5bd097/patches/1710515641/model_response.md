```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final byte[] classBytes = data.getMutatedClass().getBytes();
    final long classCRC = data.getMutatedClass().getCRC();
    final org.pitest.classinfo.ClassInfoBuilder classInfo = org.pitest.classinfo.ClassInfoVisitor.getClassInfo(data.getMutatedClass(), classBytes, classCRC);
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```