```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final org.pitest.classinfo.ClassName clazz = org.pitest.classinfo.ClassName.fromString(data.getMutatedClass());
    final byte[] bytes = coverage.getBytecode(clazz);
    final long checksum = coverage.getChecksum(clazz);
    final org.pitest.classinfo.ClassInfoBuilder info = org.pitest.classinfo.ClassInfoVisitor.getClassInfo(clazz, bytes, checksum);
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), info.build());
}
```