```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final org.pitest.classinfo.ClassName className = org.pitest.classinfo.ClassName.fromString(data.getMutatedClass());
    final byte[] classBytes = coverage.getClassBytes(className);
    final long checksum = coverage.getChecksum(className);
    final org.pitest.classinfo.ClassInfo classInfo = org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, classBytes, checksum);
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```