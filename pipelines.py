# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class EcommerceScraperPipeline:

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Remove leading and trailing whitespaces
        field_names = ['name', 'brand', 'new_price', 'old_price' 'disc_perc', 'rating']
        for field_name in field_names:
            value = adapter.get(field_name)
            if value:
                adapter[field_name] = value.strip()

        # Clean price fields
        price_keys = ['new_price', 'old_price']

        for price_key in price_keys:
            value = adapter.get(price_key)
            if value:
                value = value.replace('₦', '')
                value = value.strip()
                value = value.replace(',', '')

            adapter[price_key] = float(value)

        # Clean discount field
        value = adapter.get('disc_perc')
        if value:
            adapter['disc_perc'] = value.replace('%', '')

        # Clean rating field
        value = adapter.get('rating')
        if value:
            value_array = value.split(' ')
            rating_value = value_array[0]
            adapter['rating'] = (float(rating_value)/5.0) * 100
        

        return item
