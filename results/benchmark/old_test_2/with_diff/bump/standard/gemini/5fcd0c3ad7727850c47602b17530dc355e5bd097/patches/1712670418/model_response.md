```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final org.pitest.classinfo.ClassName clazz = new org.pitest.classinfo.ClassName(data.getMutatedClass());
    final byte[] bytes = coverage.getClassBytes(clazz);
    final long checksum = coverage.getChecksum(clazz);
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), org.pitest.classinfo.ClassInfoVisitor.getClassInfo(clazz, bytes, checksum));
}
```