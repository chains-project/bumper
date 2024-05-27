```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    java.util.Set<org.pitest.classinfo.ClassName> classNames = java.util.Collections.singleton(data.getMutatedClass());
    org.pitest.classinfo.ClassInfo classInfo = null;
    for (org.pitest.classinfo.ClassInfo info : coverage.getAllClasses()) {
        if (info.getName().equals(data.getMutatedClass())) {
            classInfo = info;
            break;
        }
    }
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```