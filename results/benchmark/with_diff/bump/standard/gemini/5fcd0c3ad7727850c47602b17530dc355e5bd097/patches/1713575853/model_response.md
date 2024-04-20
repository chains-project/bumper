```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final ClassName className = ClassName.fromString(data.getFileName());
    final ClassInfoBuilder classInfoBuilder = new ClassInfoVisitor().getClassInfo(className, data.getBytes(), data.getTime());
    final ClassInfo classInfo = classInfoBuilder.build();
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```