```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final Set<org.pitest.classinfo.ClassName> classNames = java.util.Collections.singleton(data.getMutatedClass());
    final byte[] classBytes = data.getBytes();
    final long lastModified = data.getLastModified();

    final org.pitest.classinfo.ClassInfo classInfo = org.pitest.classinfo.ClassInfoVisitor.getClassInfo(classNames.iterator().next(), classBytes, lastModified);

    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```