```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    org.pitest.classinfo.ClassName className = data.getMutatedClass();
    byte[] classBytes = coverage.getClassBytes(className);
    long classHash = coverage.getClassHash(className);
    org.pitest.classinfo.ClassInfo classInfo = org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, classBytes, classHash);
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```