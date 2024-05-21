```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final org.pitest.classinfo.ClassName mutatedClass = data.getMutatedClass();
    final byte[] bytecode = data.getBytecode();
    final long checksum = data.getChecksum();
    final org.pitest.classinfo.ClassInfo classInfo = org.pitest.classinfo.ClassInfoVisitor.getClassInfo(mutatedClass, bytecode, checksum);
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```