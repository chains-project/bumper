```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final Set<org.pitest.classinfo.ClassName> classNames = Collections.singleton(data.getMutatedClass());
    final byte[] bytes = coverage.getBytes(classNames.iterator().next());
    final long checksum = coverage.checksum(classNames.iterator().next());
    final ClassInfoBuilder classInfoBuilder = ClassInfoVisitor.getClassInfo(classNames.iterator().next(), bytes, checksum);
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfoBuilder.build());
}
```