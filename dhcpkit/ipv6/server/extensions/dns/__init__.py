"""
Handlers for the DNS options defined in dhcpkit.ipv6.extensions.dns
"""

from ipaddress import IPv6Address

from typing import List

from dhcpkit.ipv6.extensions.dns import RecursiveNameServersOption, DomainSearchListOption
from dhcpkit.ipv6.server.handlers.basic import SimpleOptionHandler


class RecursiveNameServersOptionHandler(SimpleOptionHandler):
    """
    Handler for putting RecursiveNameServersOption in responses
    """

    def __init__(self, dns_servers: List[IPv6Address]):
        option = RecursiveNameServersOption(dns_servers=dns_servers)
        option.validate()

        super().__init__(option)

    def __str__(self):
        return "{} for {}".format(self.__class__.__name__, ', '.join(map(str, self.option.dns_servers)))

    def combine(self, existing_options: List[RecursiveNameServersOption]) -> RecursiveNameServersOption:
        """
        Combine multiple options into one.

        :param existing_options: The existing options to include name servers from
        :return: The combined option
        """
        addresses = []

        # Add from existing options first
        for option in existing_options:
            for address in option.dns_servers:
                if address not in addresses:
                    addresses.append(address)

        # Then add our own
        for address in self.option.dns_servers:
            if address not in addresses:
                addresses.append(address)

        # And return a new option with the combined addresses
        return RecursiveNameServersOption(dns_servers=addresses)


class DomainSearchListOptionHandler(SimpleOptionHandler):
    """
    Handler for putting RecursiveNameServersOption in responses
    """

    def __init__(self, search_list: List[str]):
        option = DomainSearchListOption(search_list=search_list)
        option.validate()

        super().__init__(option)

    def __str__(self):
        return "{} for {}".format(self.__class__.__name__, ', '.join(self.option.search_list))

    def combine(self, existing_options: List[DomainSearchListOption]) -> DomainSearchListOption:
        """
        Combine multiple options into one.

        :param existing_options: The existing options to include domain names from
        :return: The combined option
        """
        domains = []

        # Add from existing options first
        for option in existing_options:
            for domain in option.search_list:
                if domain not in domains:
                    domains.append(domain)

        # Then add our own
        for domain in self.option.dns_servers:
            if domain not in domains:
                domains.append(domain)

        # And return a new option with the combined addresses
        return DomainSearchListOption(search_list=domains)
