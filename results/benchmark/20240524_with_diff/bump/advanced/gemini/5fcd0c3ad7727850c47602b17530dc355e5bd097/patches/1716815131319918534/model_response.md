```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final org.pitest.classinfo.ClassName mutatedClass = data.getMutatedClass();
    final byte[] classBytes = data.getBytes();
    final long checksum = data.getChecksum();
    final org.pitest.classinfo.ClassInfo classInfo = coverage.getClassInfo(mutatedClass, classBytes, checksum);
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```