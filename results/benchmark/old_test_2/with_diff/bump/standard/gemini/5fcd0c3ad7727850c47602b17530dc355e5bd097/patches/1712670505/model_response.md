```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final org.pitest.classinfo.ClassInfo classInfo = org.pitest.classinfo.ClassInfoVisitor.getClassInfo(
            org.pitest.classinfo.ClassName.fromString(data.getMutatedClass()),
            coverage.getBytecodeForClass(data.getMutatedClass()),
            coverage.getCoverageIdForClass(data.getMutatedClass()));
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```