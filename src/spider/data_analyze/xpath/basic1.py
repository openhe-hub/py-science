#%%
from lxml import etree

# %%
# build an etree object from local
tree=etree.parse('test.html')
# %%
r=tree.xpath('/html/head/title')
print(r)
# %%
r=tree.xpath('/html/body/p')
print(r)
# %%
r=tree.xpath('/html//b')
print(r)
r=tree.xpath('//b')
print(r)
# %%
r=tree.xpath('//p[@class="title"]')
print(r)
# %%
r=tree.xpath('//p[@class="title"]/b[2]')
print(r)
# %%
r=tree.xpath('//a[@id="link1"]/text()')[0]
print(r)
# %%
r=tree.xpath('//a[@id="link3"]//text()')
print(r)
# %%
r=tree.xpath('//div[2]/@class')
print(r)
# %%
