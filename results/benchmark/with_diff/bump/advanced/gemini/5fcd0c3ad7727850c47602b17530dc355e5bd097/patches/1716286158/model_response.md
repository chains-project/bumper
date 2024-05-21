```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final Set<org.pitest.classinfo.ClassName> classInfos = new HashSet<>();
    classInfos.add(data.getMutatedClass());
    final List<org.pitest.classinfo.ClassInfo> classInfoList = new ArrayList<>();
    for (final org.pitest.classinfo.ClassName className : classInfos) {
        final byte[] bytes = coverage.getBytecode(className);
        final long time = coverage.getModificationTime(className);
        if (bytes != null && time != 0) {
            classInfoList.add(org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, bytes, time));
        }
    }
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfoList);
}
```